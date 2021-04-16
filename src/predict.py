import numpy as np 
import pandas as pd 
import pickle


def predict(data, pipeline,  model_path='models/test_model.pickle'):
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
    return_data = data.copy()
    model = pickle.load(open(model_path, 'rb'))
    X = pipeline.get_X(data)
    predictions = model.predict_proba(X)
    return_data['probability'] = predictions[:,1]
    return return_data
    

