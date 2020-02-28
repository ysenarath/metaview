from typing import Text

from flask import Blueprint, render_template

from knet.config import CONFIG

bp = Blueprint('views', __name__)


@bp.route('/')
def home():
    return render_template('index.html', title=CONFIG['APP_TITLE'], page='Home')


@bp.route('/<page>')
def pages(page: Text):
    return render_template('index.html', title=CONFIG['APP_TITLE'], page=page.capitalize())
