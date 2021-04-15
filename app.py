from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, url_for, session, redirect, jsonify, render_template_string, request

app = Flask(__name__)




@app.route('/', methods=['GET'])
def home():
    """[Renders HTML homepage]

    Returns:
        [HTML]: [Project splash page]
    """    
    return render_template('index.html')
#    return ''' <p> nothing here, friend, but a link to 
#                  <a href="/hello">hello</a> and an 
#                   <a href="/form_example">example form</a> </p> '''

@app.route('/scores', methods=['POST','GET'])
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



# @app.route('/', methods=['GET'])
# def home_orig():
#    return ''' <p> nothing here, friend, but a link to 
#                  <a href="/hello">hello</a> and an 
#                   <a href="/form_example">example form</a> </p> '''



# @app.route('/form_example', methods=['GET'])
# def form_display():
#     return ''' <form action="/string_reverse" method="POST">
#                 <input type="text" name="some_string" />
#                 <input type="submit" />
#                </form>
#              '''

# @app.route('/string_reverse', methods=['POST'])
# def reverse_string():
#     text = str(request.form['some_string'])
#     reversed_string = text[-1::-1]
#     return ''' output: {}  '''.format(reversed_string)




if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)