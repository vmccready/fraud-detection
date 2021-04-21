from flask import Flask, render_template, url_for, session, redirect, jsonify, render_template_string, request
import src.pipeline as pipeline
from src.predict import predict
import pandas as pd
import numpy as np
from src.model import create_model


application = Flask(__name__)



@application.route('/', methods=['GET'])
def home():
    """[Renders HTML homepage]

    Returns:
        [HTML]: [Project splash page]
    """    
    return render_template('index.html')
#    return ''' <p> nothing here, friend, but a link to 
#                  <a href="/hello">hello</a> and an 
#                   <a href="/form_example">example form</a> </p> '''


@application.route('/summary', methods=['GET'])
def summary():
    """[This is a good example of simply switching pages.
        The '/summary' route being navigated to (above) activates
        'display()' which calls/returns 'render_template()'.
        This in turn retreives a specified html file, which in this case
        has a line stating that it extends the 'base' html page.
        It is this 'base' html page that is rendered with the contents
        of 'summary.html' inserted.]

    Returns:
        [function]: [HTML(fictional summary for project narrative)]
    """
    return render_template('summary.html')



@application.route('/scores', methods=['POST','GET'])
def display_scores():
    """[reads data, processes through models, predict.

        
        
        ]

    Returns:
        [function]: [HTML(template built to display a dict as a table)]
    """
    # output can be k:v, list, nested, etc. jinja can do indexing and deal with nesting.

    # Read in data
    api_df =  pd.read_json('data/api_data.json')
    # Set model location as variable
    model_path = 'models/rf_1.pickle'
    # Store model.predict into 'scores'
    scores = predict(api_df, pipeline, model_path)
    # Set columns names
    scores = scores[['object_id','org_name','country','name','payee_name','payout_type','probability']]
    # Add a computed column ('risk'), with categorical values
    scores['risk'] = scores['probability'].apply(lambda p: 'HIGH' if p > .85 else 'MEDIUM' if p > .8 else 'LOW')
    # Round values in 'probability' column
    scores['probability'] = np.round(scores['probability'],2)


    scores = scores.values

    return render_template('scores.html', scores=scores)


# run the app.
if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    application.debug = True
    application.run()



