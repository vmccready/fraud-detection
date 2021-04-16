import numpy as np 
import pandas as pd 
import pickle

from sklearn.linear_model import LogisticRegression

# Path to saved trained model
model_path = '../models/model.pickle'

def get_X(df):
    mask = df.previous_payouts.apply(lambda x: 0 if len(x) <= 0 else 1)
    df['mask_previous_payout'] = mask
    X = df[['mask_previous_payout', 'user_age']]
    return X

def predict(model_path, data):
    '''
    Takes a path to trained model and case to detect fraud. Returns probability
    of fraud. 

    Input:
        model_path(str) - string of path to trained model
        data(pd.Dataframe) - Pandas dataframe of data returned from api. Has 
                case of potential fraud.
    
    Output: 
        probabilities(arr) - array of probabilities of outcomes. 
                0 column is Not Fraud, 1 column is Fraud
    '''
    model = pickle.load(open(model_path, 'rb'))
    X = get_X(data)
    predictions = model.predict_proba
    

