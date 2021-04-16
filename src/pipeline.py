import pandas as pd

# ---------------------------------------------------------------------------
# Pipeline Funtions 
# ---------------------------------------------------------------------------
def not_premium(x):
    return 1 if x.lower() != 'premium' else 0

def no_previous_payout(x):
    return 1 if len(x) <= 0 else 0

def payout_name_flag(x):
    for d in x:
        if len(d['name']) > 3:
            return 1
    return 0

def payout_toself(payee, payouts):
    for pay in payouts:
        if payee.lower() in pay['name'].lower():
            return 1
    return 0

# ---------------------------------------------------------------------------
# End Funtions 
# ---------------------------------------------------------------------------
# 

def get_X(df):
    temp = dict()
    temp = {'previous_payout': df.previous_payouts.apply(lambda x: no_previous_payout(x)),
    #         'premium': df.acct_type.apply(lambda x: not_premium(x)),
            'no_payout_name': df.previous_payouts.apply(lambda x: payout_name_flag(x)),
            'payout_toself': df.apply(lambda x: payout_toself(x.payee_name, x.previous_payouts), axis = 1),
            'account_type' : df['user_type'],
            'delivery_method' : df['delivery_method']}

    df_model = pd.DataFrame(temp)
    # we filled nan values with 0 because more fradulent users 
    # had missing values, and most fradulant users 
    # have a delivery method of 0
    df_model['delivery_method'] = df['delivery_method'].fillna(0)
    # venue name 
    X = df_model.copy()
    # X = df_model.drop('target', axis = 1)
    X['user_age'] = df['user_age']

    return X
    
def get_y(df):
    df['fraud'] = df.acct_type.apply(lambda x: 1 if 'fraud' in x else 0)
    temp = dict()
    temp = {'target': df['fraud'].copy()}

    df_model = pd.DataFrame(temp)

    y = df_model['target']
    return y
    
