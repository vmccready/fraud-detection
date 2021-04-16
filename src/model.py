import numpy as np 
import pandas as pd 
import pickle

# from pipeline import get_X, get_y

from sklearn.ensemble import RandomForestClassifier

# BEST MODEL
# features - 'previous_payout', 'premium', 'no_payout_name', 
# 'payout_toself', 'user_age'
def create_model(data, pipeline,  model_path='models/test_model.pickle'):
    '''
    Takes raw training data as dataframe, runs through pipeline, and trains a model. 

    Input: 
        data (pd.DataFrame) - Dataframe of raw training data that has been read 
            in from json file. 
    
    Output: 
        returns none - best model will be saved to models folder
    '''

    # Create X and y from raw data
    X = pipeline.get_X(data)
    y = pipeline.get_y(data)

    # Create and train model
    model = RandomForestClassifier()
    model.fit(X,y)

    # Output model as pickle file to input path. 
    pickle.dump(model, open(model_path, 'wb'))