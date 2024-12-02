import json
from json import dumps

from flask import render_template, request, session, redirect

from app.list import list

@list.route('/list')
def list_view():
    return render_template('/test.html')