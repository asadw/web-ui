"""
Testing flask web app
"""

import sys
from datetime import datetime
from flask import Flask
from mako.lookup import TemplateLookup

TEMPLATES = 'templates/' if sys.platform.startswith("win") else './admin/templates/'
LOOKUP = TemplateLookup(directories=[TEMPLATES])
APP = Flask(__name__)

@APP.route('/', methods=['GET'])
def login():
    """ login page """
    return LOOKUP.get_template('login.html').render()


@APP.route('/admin', methods=['GET'])
def hello_world():
    """
    Just a test function to serve a simple page w/ a timestamp
    """

    the_time = datetime.now().strftime("%b %d %Y %I:%M:%S%p")
    return LOOKUP.get_template('hello.html').render(name="TEST", t=the_time)
