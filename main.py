from flask import Flask, request, redirect, render_template
import cgi
import os
import jinja2

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape=True)



app = Flask(__name__)
app.config['DEBUG'] = True


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/welcome", methods=['POST'])
def welcome():
    user_name= request.form['user_name']
    return render_template('welcome.html', username=username)



@app.route('/validate-user')
def display_user_form():
    return render_template('index.html')



@app.route('/', methods=['POST'])
def validate_user():
    uname = request.form['username']
    passwd = request.form['password']
    vpasswd = request.form['verify_password']
    myemail = request.form['email']
    uname_error = ''
    passwd_error = ''
    vpasswd_error = ''
    myemail_error = ''            

    # The user leaves any of the following fields empty: username, 
    # password, verify password.
    
    if not uname:
        uname_error = 'Username is blank'
    else:
        if len(uname) < 3 or len(uname) > 20:
            uname_error = 'Username must be between 3 and 20 characters'
    
    if not passwd:
        passwd_error = 'Password is blank'
    else:
        if len(passwd) < 3 or len(passwd) > 20:
            passwd_error = 'Password must be between 3 and 20 characters'
            passwd=''
    
    if not vpasswd:
        vpasswd_error = 'Password validation is blank'
    
    # The user's username or password is not valid -- for example, 
    # it contains a space character or it consists of less than 3 
    # characters or more than 20 characters (e.g., a username or 
    # password of "me" would be invalid).
    
    if ' ' in uname:
        uname_error = 'Username must not contain blank spaces'
    #if len(uname) < 3 or len(uname) > 20:
    #    uname_error = 'Username must be between 3 and 20 characters'
    if ' ' in passwd:
        passwd_error = 'Password must not contain blank spaces'
        passwd = ''
    #else:
    #    if len(passwd) < 3 or len(passwd) > 20:
    #        passwd_error = 'Password must be between 3 and 20 characters'
    #        passwd = ''
        
    # The user's password and password-confirmation do not match.
    if passwd != vpasswd:
        passwd_error = 'Passwords do not match'
    
    
    # The user provides an email, but it's not a valid email. 
    # Note: the email field may be left empty, but if there is 
    # content in it, then it must be validated. 
    # The criteria for a valid email address in this assignment 
    # are 
    
    # that it has a single @, a single ., 
    
    if myemail:
        if not myemail.count('@') == 1:
            myemail_error = 'Email must contain 1 "@" sign'

        if not myemail.count('.') == 1:
            myemail_error = 'Email must contain 1 "."'
        
        #contains no spaces
        if " " in myemail:
            myemail_error = 'Email must not contain spaces' 

        #and is between 3 and 20 characters long
        if len(myemail) < 3 or len(uname) > 20:
            myemail_error = 'Email must be between 3 and 20 characters long'


    if not uname_error and not passwd_error and not vpasswd_error and not myemail_error:            
        #username=uname
        return render_template('welcome.html', username=uname)
    else:
        return render_template('index.html', email=myemail, username=uname, username_error=uname_error, password_error=passwd_error, verify_password_error=vpasswd_error, email_error=myemail_error)



@app.route('/welcome')
def valid_user():
    uname = request.args.get('')
    return redirect('welcome.html')


app.run()