import os
import os.path
from flask import Flask, flash, redirect, render_template, \
     request, url_for, g
import os

from flask_bootstrap import Bootstrap


UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), 'static')

path = os.path.join(os.path.dirname(__file__), 'static')


#mail = Mail()

# Create Flask application
app = Flask(__name__)

# Bootstrap init
Bootstrap(app)


# Create customized index view class that handles login & registration
# The application is to the client's specification
# Once the application is approved by an admin, the admin sends an email with an access code
# The access code can be the same for every user if it takes less dev time
# The access code is used to authorize the user to register for the site

@app.route('/contact')
def contact():
   return render_template('contact.html')


# Main function
@app.route('/')
def home():
    return render_template('home.html') #ripped from wordpress

@app.route('/services')
def services():
    return render_template('services.html') #ripped from wordpress

# @app.route('/contact')
# def contact():
#     return render_template('contact.html') #ripped from wordpress

@app.route('/classes')
def classes():
    return render_template('classes.html')

@app.route('/resources')
def resources():
    return render_template('resources.html') #ripped from wordpress



    # Start app
    app.run(debug=True)