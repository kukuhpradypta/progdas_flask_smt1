from flask import Blueprint

list = Blueprint('list', __name__)

from . import view
from . import api
