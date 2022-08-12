#Import packages
import pandas as pd
from util.dataloader import DataLoader
from util.datasplitter import data_splitter
from preprocessing.preprocessor import Preprocessor
from preprocessing.fasttext_embeddings import FastTextEmbeddings
from evaluator import evaluate_classifier, get_summary_dataset
from nltk import download
import warnings
warnings.filterwarnings('ignore')
import os

#Load model configurations with best hyperparameters
from config.best_params import best_params

#Set SEED
SEED=42

def run_task(task, 
             save_model=True,
             track_carbon=False):
    '''
    Train and evaluates all models on all datasets for a particular task. 
    Args:
        task (str): the selected task, can be any of ['fake_news','topic','emotion','polarity','sarcasm']
        save_model (bool): if True, saves the trained models as .sav files with pickle.
        track_carbon (bool): if True, activates a carbon tracker while training the models 
    '''
    #Load data
    dl = DataLoader([task])
    task_data = dl.load()
    #Initialize preprocessor
    preprocessor=Preprocessor()
    tweet_preprocessor=Preprocessor(is_tweet=True)
    #Load fasttext 
    fasttext = FastTextEmbeddings()
    fasttext.load_model('fasttext/cc.en.300.bin')

    for k in task_data.keys():
        #Iterate through all the datasets for the specified task
        if k in ['SemEval_A','SemEval_B','iSarcasm','tweetEval']: #Tweet datasets require tweet preprocessor
            train, _ , test = data_splitter(task_data[k],tweet_preprocessor,
                                            create_val_set=True,seed=SEED)
        else:
            train, _ , test = data_splitter(task_data[k],preprocessor,
                                            create_val_set=True,seed=SEED)
        #Generate sentence embeddings                                   
        embedded_train = fasttext.generate_sentence_embeddings(train['text']).fillna(0)
        embedded_test = fasttext.generate_sentence_embeddings(test['text']).fillna(0)
        embedded_train['label'] =  train['label'].to_list()
        embedded_test['label'] = test['label'].to_list()
        #Evaluate and save the model, save the metrics and predictions on test set as csv
        _, _ = get_summary_dataset(k,train,test, embedded_train,embedded_test,best_params[k], 
                                   save_model=save_model, track_carbon=track_carbon)
        print('Evaluation completed for dataset : ' + k)
        

if __name__=='__main__':

    #Load linguistic resources
    download('stopwords', quiet=True)
    download('omw-1.4', quiet=True)
    download('punkt', quiet=True)
    download('wordnet', quiet=True)
    #Create an output folder
    if not os.path.isdir('output'):
        os.makedirs('output')

    run_task('fake_news')
    # run_task('topic')
    # run_task('emotion')
    # run_task('polarity')
    # run_task('sarcasm')