from flask import Flask, render_template, url_for, session, redirect, jsonify, render_template_string, request
import src.pipeline as pipeline
from src.predict import predict
import pandas as pd
import numpy as np
from src.model import create_model

# print a nice greeting.
def say_hello(username = "World"):
    return '<p>Hello %s!</p>\n' % username

# some bits of text for the page.
header_text = '''
    <html>\n<head> <title>EB Flask Test</title> </head>\n<body>'''
instructions = '''
    <p><em>Hint</em>: This is a RESTful web service! Append a username
    to the URL (for example: <code>/Thelonious</code>) to say hello to
    someone specific.</p>\n'''
home_link = '<p><a href="/">Back</a></p>\n'
footer_text = '</body>\n</html>'

# EB looks for an 'application' callable by default.
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


@application.route('/scores', methods=['POST','GET'])
def display_scores():
    """[Formats and renders]

    Returns:
        [HTML,iterable datastructure]: []
    """    
    # can be k:v, list, nested, etc. jinja can do indexing
    # the below is an example/placeholder

    api_df =  pd.read_json('data/api_data.json') 
    model_path = 'models/rf_1.pickle'
    scores = predict(api_df, pipeline, model_path)
    head = scores.columns
    scores = scores[['object_id','org_name','country','name','payee_name','payout_type','probability']]
    scores['risk'] = scores['probability'].apply(lambda p: 'HIGH' if p > .85 else 'MEDIUM' if p > .8 else 'LOW')
    scores['probability'] = np.round(scores['probability'],2)


    scores = scores.values

    return render_template('scores.html', scores=scores, head=head)


# run the app.
if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    application.debug = True
    application.run()



