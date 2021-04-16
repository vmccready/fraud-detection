from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, url_for, session, redirect, jsonify, render_template_string, request

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
    scores = {'123456':['Missing Data, History of Fraud, Steals Candies', 'Linear Regression',    
        '2695',
        '99']}
    return render_template('scores.html', scores=scores)


# run the app.
if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    application.debug = True
    application.run()



