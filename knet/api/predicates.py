from collections import defaultdict

from flask import request
from flask_restful import Resource

from knet.config import CONFIG
from knet.models.graph import open_graph


# noinspection PyMethodMayBeStatic,PyBroadException
class Predicates(Resource):
    def get(self):
        limit = defaultdict(lambda: None, **request.args)['limit']
        results = []
        with open_graph(CONFIG['RDF_PATH']) as g:
            if limit is not None and isinstance(limit, int):
                g = g[:limit]
            for subj, pred, obj in g:
                results.append(dict(subject=subj, predicate=pred, object=obj))
        return results
