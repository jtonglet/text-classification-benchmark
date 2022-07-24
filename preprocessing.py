#Import packages
import matplotlib.pyplot as plt
from nltk.tokenize import word_tokenize, TweetTokenizer
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk import download
import re
from time import time
import emoji 

#Load linguistics resources
download('stopwords')
download('omw-1.4')



class Preprocessor:

    def __init__(self,
                 is_tweet=False,
                 lemmatizer = WordNetLemmatizer(),
                 stopwords = stopwords.words('english'),
                 emojis = emoji.UNICODE_EMOJI_ENGLISH):

        self.is_tweet = is_tweet
        self.lemmatizer = lemmatizer
        self.stopwords = stopwords
        self.emojis = emojis
    
    def remove_unicode(self,text):
        #Remove unicode characters from text
        return text.encode('ascii','ignore').decode()

    def remove_punct(self,text):
        #Remove punctuation from string text
        punctuation = "!\"$%&'()*+,-?.../:;<=>[\]^_`{|}~#@"
        text = ''.join(char for char in text if char not in punctuation)
        return text

    # def remove_emojis(self,text):
    #     #Remove emojis from string text
    #     text = re.compile(pattern = "["
    #     u"\U0001F600-\U0001F64F"  # emoticons
    #     u"\U0001F300-\U0001F5FF"  # symbols & pictographs
    #     u"\U0001F680-\U0001F6FF"  # transport & map symbols
    #     u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
    #                        "]+", flags = re.UNICODE).sub(r'',text)    
                                 
    #     return text
    
    def remove_repeated_letters(self, text):
        #If the same letters appears consecutively 3 times or more, reduce it to 1 occurence  (WIP implementation)
        text = re.compile(r'(.)\1{2,}', re.IGNORECASE).sub(r'\1',text)
        return text

    def tokenize(self,text):
        #Tokenize the text
        if self.is_tweet:
            return TweetTokenizer().tokenize(text)
        else:
            return word_tokenize(text)


    def drop_digits(self,text):
        #Remove numbers from tokenized text
        text = [word for word in text if not word.isdigit()]
        return text

    def drop_emojis(self,text):
        #Remove (sequence of) emojis from tokenized text
        text = [word for word in text if word[0] not in self.emojis] #If there is more than one emoji in the word token, just check the first one
        return text
        
    def drop_stopwords(self,text):
        #Remove stopwords from tokenized text
        text = [word for word in text if word not in self.stopwords]
        return text

    def drop_urls(self,text):
        #Remove urls from tokenized text
        text = [word for word in text if 'http' not in word]
        return text 
    
    def lemmatize(self,text):
        #Lemmatize text 
        text = [self.lemmatizer.lemmatize(word) for word in text]
        return text

    def preprocess(self,df):
        #Full preprocessing pipeline for a corpus
        start_time = time()
        corpus = df['text'].fillna('').str.lower().to_list()
        corpus = [self.remove_unicode(text) for text in corpus]
        corpus = [self.remove_punct(text) for text in corpus]
        corpus = [self.remove_repeated_letters(text) for text in corpus]
        corpus = [self.tokenize(text) for text in corpus]
        corpus = [self.drop_digits(text) for text in corpus]
        corpus = [self.drop_stopwords(text) for text in corpus]
        corpus = [self.drop_emojis(text) for text in corpus]
        corpus = [self.drop_urls(text) for text in corpus]
        corpus = [self.lemmatize(text) for text in corpus]
        corpus = [' '.join(text) for text in corpus]
        
        print('%s rows preprocessed in %s seconds'%(df.shape[0],time()-start_time))
        return corpus
