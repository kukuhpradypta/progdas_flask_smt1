from flask import Blueprint

home = Blueprint('home', __name__)

from . import view
from . import api
from . import model
