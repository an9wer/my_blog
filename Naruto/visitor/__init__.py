from flask import Blueprint

visitor = Blueprint('visitor',
					__name__,
					template_folder='templates',
					static_folder='static',
					static_url_path='/visitor/static')

from . import views
