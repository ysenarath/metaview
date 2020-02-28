from flask import Blueprint
from flask_restful import Api

from .predicates import Predicates
from .query import Query

bp = Blueprint('api', __name__)
api = Api(bp)

api.add_resource(Predicates, '/predicates')
api.add_resource(Query, '/query')
