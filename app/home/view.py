import json
from json import dumps

from flask import render_template, request, session, redirect

from app.home import home

@home.route('/')
def home_view():
    return render_template('/home.html')