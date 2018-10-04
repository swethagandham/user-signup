from flask import Flask, request, render_template, redirect
import cgi
import re


app = Flask(__name__)

app.config['DEBUG'] = True

@app.route("/")
def index():
    encodederror = request.args.get("error")
    return render_template('index.html')

@app.route("/formvalidate", methods=['POST'])  
def form_validate():
    username = request.form['username']
    password = request.form['password']
    verifypassword = request.form['verifypassword']
    email = request.form['email']
    empty = " "
    username_error = ""
    password_error = ""
    verifypassword_error = ""
    email_error = ""


    if username =="" or username ==" " or (empty in username) == True or len(username)<3 or len(username)>20:
        username_error = "That is not valid username"
        username = ""


    if password =="" or password ==" " or (empty in password) == True or len(password)<3 or len(password)>20:
        password_error = "That is not valid password"
        password = ""

    if verifypassword != password:
        verifypassword_error = "password is not match"
        verifypassword = ""

    regex_str = "^(?=.{3,20}$)[a-zA-Z0-9]+@[a-zA-Z0-9]+\.[a-zA-Z]+$"
    x = re.search(regex_str,email)

    
    if email != '':
        if not x:
            email_error = "That is not a valid email"
            email = ""

    if not username_error and not password_error and not verifypassword_error and not email_error:
        return render_template('welcome.html', username=username)

    return render_template('index.html', username_error=username_error,
        password_error=password_error, verifypassword_error=verifypassword_error, email_error=email_error, username=username,email=email)


app.run()            

