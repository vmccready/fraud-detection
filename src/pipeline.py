import pandas as pd
import math 


# ---------------------------------------------------------------------------
# Pipeline Funtions 
# ---------------------------------------------------------------------------
def missing_data(x):
    '''
    Param:
        x: dictionary
    Return:
        1 if missing value is found else 0
    '''
    for value in x.values():
        if value == '':
            return 1
    return 0

def no_previous_payout(x):
    '''
    Param:
        list of previous payouts 
    '''
    return 1 if len(x) <= 0 else 0

def payout_name_flag(x):
    '''
    Param:
        list of previous payouts 
    '''
    for d in x:
        if len(d['name']) < 3:
            return 1
    return 0

def payout_toself(payee, payouts):
    '''
    Param:
        payee: payee 
        payouts: list of previous payouts 
    '''
    for pay in payouts:
        if payee.lower() in pay['name'].lower():
            return 1
    return 0

def payee_name_flag(x):
    return 1 if len(x) < 3 else 0

def delivery(x):
    if math.isnan(x): return 0
    return int(x)

def parse_data(data):
    '''
        Param:
            api data call
    '''
    temp = dict()
    
    if type(data) == type(dict()):
        temp = {
            'payout_toself': payout_toself(data['payee_name'], data['previous_payouts']),
            'missing_data': missing_data(data),
            'previous_payout': no_previous_payout(data['previous_payouts']),
            'no_payout_name': payout_name_flag(data['previous_payouts']),
            'no_payee_name': payee_name_flag(data['payee_name']),
            'account_type': data['user_type'],
            'delivery_method': delivery(data['delivery_method']),
            'user_age': data['user_age']}
    else:
        temp = {
            'payout_toself': data.apply(lambda x: payout_toself(x.payee_name, x.previous_payouts), axis = 1),
            'missing_data': data.isnull().any(axis = 1) * 1,
            'previous_payout': data.previous_payouts.apply(lambda x: no_previous_payout(x)),
            'no_payout_name': data.previous_payouts.apply(lambda x: payout_name_flag(x)),
            'no_payee_name': data.payee_name.apply(lambda x: payee_name_flag(x)),
            'account_type': data.user_type,
            'delivery_method': data.delivery_method.apply(lambda x: delivery(x)),
            'user_age': data.user_age }
    
    return temp
# ---------------------------------------------------------------------------
# End Funtions 
# ---------------------------------------------------------------------------

def get_X(df):
    temp = parse_data(df)
    df_model = pd.DataFrame(temp)

    return df_model.copy()
    
def get_y(df):
    df['fraud'] = df.acct_type.apply(lambda x: 1 if 'fraud' in x else 0)
    temp = dict()
    temp = {'target': df['fraud'].copy()}

    df_model = pd.DataFrame(temp)

    y = df_model['target']
    return y
    
