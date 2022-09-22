#Import packages
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC, LinearSVC
from xgboost import XGBClassifier

#set seed for reproducibility
SEED=42

'''
This python file is used to store the best hyperparameters configurations for all models. It consists in a nested dictionary 
where the first-level keys correspond to the dataset names, and the sub-keys correspond to a machine learning model with specified best params.

!!Important naming convention!!: if the model requires tf-idf preprocessing, the character sequence 'tfidf' needs to appear in the subkey.
'''

best_params = {}


#to do : xgb
best_params['gossipcop'] = {'tfidf_lr':LogisticRegression(C=8.959,random_state=SEED),
                     'ft_lr':LogisticRegression(C=7.346,random_state=SEED),
                     'tfidf_rf':RandomForestClassifier(n_estimators=44,max_features='sqrt',random_state=SEED),
                     'ft_rf':RandomForestClassifier(n_estimators=94,max_features='sqrt',random_state=SEED),
                     'tfidf_svm':SVC(probability=True,kernel='linear',C=1.145,random_state=SEED),
                     'ft_svm':SVC(probability=True,kernel='rbf',C=8.34,random_state=SEED),
                     'tfidf_xgb':XGBClassifier(gamma=,learning_rate=,max_depth=,n_estimators=,random_state=SEED),
                     'ft_xgb':XGBClassifier(gamma=,learning_rate=,max_depth=,n_estimators=,random_state=SEED)
                           }

#to do : b
best_params['liar'] = {'tfidf_lr':LogisticRegression(C=4.376,random_state=SEED),
                     'ft_lr':LogisticRegression(C=7.82,random_state=SEED),
                     'tfidf_rf':RandomForestClassifier(n_estimators=121,max_features='sqrt',random_state=SEED),
                     'ft_rf':RandomForestClassifier(n_estimators=94,max_features='log2',random_state=SEED)
                     'tfidf_svm':SVC(probability=True,kernel='linear',C=2.956,random_state=SEED),
                     'ft_svm':SVC(probability=True,kernel='rbf',C=9.637,random_state=SEED),
                     'tfidf_xgb':XGBClassifier(gamma=,learning_rate=,max_depth=,n_estimators=,random_state=SEED),
                     'ft_xgb':XGBClassifier(gamma=,learning_rate=,max_depth=,n_estimators=,random_state=SEED)
                      }


#done
best_params['tweetEval'] = {'tfidf_lr':LogisticRegression(C=5.064,random_state=SEED),
                         'ft_lr':LogisticRegression(C=2.11,random_state=SEED),
                            'tfidf_rf':RandomForestClassifier(n_estimators=187,max_features='log2',random_state=SEED),
                            'ft_rf':RandomForestClassifier(n_estimators=28,max_features='sqrt',random_state=SEED),
                           'tfidf_svm':SVC(probability=True,kernel='rbf',C=9.4,random_state=SEED),
                     'ft_svm':SVC(probability=True,kernel='rbf',C=5.883,random_state=SEED),
                        'tfidf_xgb':XGBClassifier(gamma=0.6745,learning_rate=0.0551,max_depth=8,n_estimators=149,random_state=SEED),
                     'ft_xgb':XGBClassifier(gamma=0.899,learning_rate=0.0379,max_depth=6,n_estimators=59,random_state=SEED)
                           }

#Done
best_params['CARER'] = {'tfidf_lr':LogisticRegression(C=8.9,random_state=SEED),
                         'ft_lr':LogisticRegression(C=8.355,random_state=SEED),
                        'tfidf_rf':RandomForestClassifier(n_estimators=67,max_features='sqrt',random_state=SEED),
                            'ft_rf':RandomForestClassifier(n_estimators=42,max_features='sqrt',random_state=SEED),
                           'tfidf_svm':SVC(probability=True,kernel='linear',C=1.67,random_state=SEED),
                     'ft_svm':SVC(probability=True,kernel='rbf',C=4.797,random_state=SEED),
                        'tfidf_xgb':XGBClassifier(gamma=0.626,learning_rate=0.0942,max_depth=8,n_estimators=121,random_state=SEED),
                     'ft_xgb':XGBClassifier(gamma=0.982,learning_rate=0.0833,max_depth=6,n_estimators=101,random_state=SEED)
                           }

#to do : xgb ft
best_params['silicone'] = {'tfidf_lr':LogisticRegression(C=6.277,random_state=SEED),
                     'ft_lr':LogisticRegression(C=8.173,random_state=SEED),
                     'tfidf_rf':RandomForestClassifier(n_estimators=93,max_features='sqrt',random_state=SEED),
                     'ft_rf':RandomForestClassifier(n_estimators=191,max_features='sqrt',random_state=SEED)
                     'tfidf_svm':LinearSVC(C=0.6963,loss='hinge',random_state=SEED),
                     'ft_svm':LinearSVC(C=9.853,loss='hinge',random_state=SEED),
                     'tfidf_xgb':XGBClassifier(gamma=0.041,learning_rate=0.0767,max_depth=10,n_estimators=150,random_state=SEED),
                     'ft_xgb':XGBClassifier(gamma=,learning_rate=,max_depth=,n_estimators=,random_state=SEED)
                      }

#Done
best_params['imdb'] = {'tfidf_lr':LogisticRegression(C=8.99,random_state=SEED),
                     'ft_lr':LogisticRegression(C=9.752,random_state=SEED),
                     'tfidf_rf':RandomForestClassifier(n_estimators=181,max_features='log2',random_state=SEED),
                     'ft_rf':RandomForestClassifier(n_estimators=119,max_features='sqrt',random_state=SEED)
                     'tfidf_svm':LinearSVC(C=0.4577,loss='hinge',random_state=SEED),
                     'ft_svm':LinearSVC(C=9.328, loss='hinge',random_state=SEED),
                        'tfidf_xgb':XGBClassifier(gamma=0.5457,learning_rate=0.0762,max_depth=7,n_estimators=148,random_state=SEED),
                     'ft_xgb':XGBClassifier(gamma=0.2529,learning_rate=0.0998,max_depth=5,n_estimators=103,random_state=SEED)
                      }

#
best_params['yelp'] = {'tfidf_lr':LogisticRegression(C=3.327,random_state=SEED),
                     'ft_lr':LogisticRegression(C=8.537,random_state=SEED),
                     'tfidf_rf':RandomForestClassifier(random_state=SEED),
                     'ft_rf':RandomForestClassifier(random_state=SEED)
                     'tfidf_svm':LinearSVC(C=0.4577,loss='hinge',random_state=SEED),
                     'ft_svm':LinearSVC(C=6.779, loss='hinge',random_state=SEED),
                        'tfidf_xgb':XGBClassifier(gamma=0.2416,learning_rate=0.0837,max_depth=9,n_estimators=100,random_state=SEED),
                     'ft_xgb':XGBClassifier(gamma=,learning_rate=,max_depth=,n_estimators=,random_state=SEED)
                      }

#Done
best_params['sst2'] = {'tfidf_lr':LogisticRegression(C=3.833,random_state=SEED),
                     'ft_lr':LogisticRegression(C=9.278,random_state=SEED),
                     'tfidf_rf':RandomForestClassifier(n_estimators=113,max_features='log2',random_state=SEED),
                     'ft_rf':RandomForestClassifier(n_estimators=149,max_features='sqrt',random_state=SEED)
                     'tfidf_svm':LinearSVC(C=0.2439,loss='hinge',random_state=SEED),
                     'ft_svm':LinearSVC(C=6.517, loss='hinge',random_state=SEED),
                        'tfidf_xgb':XGBClassifier(gamma=0.6444,learning_rate=0.0648,max_depth=9,n_estimators=150,random_state=SEED),
                     'ft_xgb':XGBClassifier(gamma=0.316,learning_rate=0.0594,max_depth=8,n_estimators=130,random_state=SEED)
                      }

#Done
best_params['iSarcasm'] = {'tfidf_lr':LogisticRegression(C=7.976,random_state=SEED),
                     'ft_lr':LogisticRegression(C=9.278,random_state=SEED),
                     'tfidf_rf':RandomForestClassifier(n_estimators=139,max_features='sqrt',random_state=SEED),
                     'ft_rf':RandomForestClassifier(n_estimators=54,max_features='log2',random_state=SEED)
                     'tfidf_svm':SVC(kernel='linear',C=2.87,probability=True,random_state=SEED),
                     'ft_svm':SVC(kernel='rbf',C=9.08,probability=True,random_state=SEED),
                     'tfidf_xgb':XGBClassifier(gamma=0.528,learning_rate=0.0727,max_depth=9,n_estimators=148,random_state=SEED),
                       'ft_xgb':XGBClassifier(gamma=0.5616,learning_rate=0.0938,max_depth=5,n_estimators=117,random_state=SEED)
                      }

#Done
best_params['SemEvalA'] = {'tfidf_lr':LogisticRegression(C=1.898,random_state=SEED),
                     'ft_lr':LogisticRegression(C=4.93,random_state=SEED),
                     'tfidf_rf':RandomForestClassifier(n_estimators=62,max_features='sqrt',random_state=SEED),
                     'ft_rf':RandomForestClassifier(n_estimators=100,max_features='log2',random_state=SEED)
                     'tfidf_svm':SVC(kernel='linear',C=4.489,probability=True,random_state=SEED),
                     'ft_svm':SVC(kernel='rbf',C=3.143,probability=True,random_state=SEED),
                       'tfidf_xgb':XGBClassifier(gamma=0.8192,learning_rate=0.06548,max_depth=10,n_estimators=138,random_state=SEED),
                     'ft_xgb':XGBClassifier(gamma=0.9532,learning_rate=0.0551,max_depth=5,n_estimators=67,random_state=SEED)
                      }

#to do all
best_params['SARC'] = {'tfidf_lr':LogisticRegression(random_state=SEED),
                     'ft_lr':LogisticRegression(random_state=SEED),
                     'tfidf_rf':RandomForestClassifier(random_state=SEED),
                     'ft_rf':RandomForestClassifier(random_state=SEED)
                     'tfidf_svm':LinearSVC(random_state=SEED),
                     'ft_svm':LinearSVC(random_state=SEED),
                     'tfidf_xgb':XGBClassifier(random_state=SEED),
                     'ft_xgb':XGBClassifier(random_state=SEED)
                      }

#to do XGB
best_params['twentynews'] = {'tfidf_lr':LogisticRegression(C=3.86,random_state=SEED),
                     'ft_lr':LogisticRegression(C=8.4,random_state=SEED),
                     'tfidf_rf':RandomForestClassifier(n_estimators=182,max_features='log2',random_state=SEED),
                     'ft_rf':RandomForestClassifier(n_estimators=127,max_features='sqrt',random_state=SEED)
                     'tfidf_svm':SVC(kernel='rbf',C=6.245,probability=True,random_state=SEED),
                     'ft_svm':SVC(kernel='rbf',C=4.682,probability=True,random_state=SEED),
                     'tfidf_xgb':XGBClassifier(gamma=0.06291,learning_rate=0.05459,max_depth=8,n_estimators=113,random_state=SEED),
                     'ft_xgb':XGBClassifier(gamma=0.6993,learning_rate=0.06194,max_depth=8,n_estimators=120,random_state=SEED)
                      }

#to do XGB
best_params['agnews'] = {'tfidf_lr':LogisticRegression(C=1.114,random_state=SEED),
                     'ft_lr':LogisticRegression(C=3.741,random_state=SEED),
                     'tfidf_rf':RandomForestClassifier(n_estimators=188,max_features='log2',random_state=SEED),
                     'ft_rf':RandomForestClassifier(n_estimators=167,max_features='log2',random_state=SEED)
                     'tfidf_svm':LinearSVC(C=1.843,loss='hinge',random_state=SEED),
                     'ft_svm':LinearSVC(C=9.337,loss='hinge',random_state=SEED),
                     'tfidf_xgb':XGBClassifier(gamma=,learning_rate=,max_depth=,n_estimators=,random_state=SEED),
                     'ft_xgb':XGBClassifier(gamma=,learning_rate=,max_depth=,n_estimators=,random_state=SEED)
                      }

#to do : rf, svc, xgb
best_params['yahoo'] = {'tfidf_lr':LogisticRegression(C=5.9,random_state=SEED),
                     'ft_lr':LogisticRegression(C=2.671,random_state=SEED),
                     'tfidf_rf':RandomForestClassifier(random_state=SEED),
                     'ft_rf':RandomForestClassifier(random_state=SEED)
                     'tfidf_svm':LinearSVC(random_state=SEED),
                     'ft_svm':LinearSVC(random_state=SEED),
                     'tfidf_xgb':XGBClassifier(gamma=,learning_rate=,max_depth=,n_estimators=,random_state=SEED),
                     'ft_xgb':XGBClassifier(gamma=,learning_rate=,max_depth=,n_estimators=,random_state=SEED)
                      }
