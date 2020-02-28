from collections import defaultdict

import pyparsing
from flask import request
from flask_restful import Resource

from knet.config import CONFIG
from knet.models.graph import open_graph


# noinspection PyMethodMayBeStatic,PyBroadException
class Query(Resource):
    def get(self):
        query = defaultdict(lambda: None, **request.args)['q']
        # limit = defaultdict(lambda: None, **request.args)['limit']
        results = []
        with open_graph(CONFIG['RDF_PATH']) as g:
            if query is not None:
                query = query.strip('"\'')
                try:
                    res = g.query(query)
                except pyparsing.ParseException:
                    return {
                        'status': 401,
                        'developerMessage': "Query parse exception occurred when evaluating the query. "
                                            "Input: %s" % query,
                        "userMessage": "You have entered an invalid query. Please enter a valid SPARQL query.",
                        "errorCode": "PE99999",
                        "moreInfo": "Please contact the developer for more information.",
                    }
                except Exception as ex:
                    if str(ex).startswith('Unknown namespace prefix'):
                        return {
                            'status': 401,
                            'developerMessage': "%s. "
                                                "Input: %s" % (str(ex), query),
                            "userMessage": "You have entered an invalid query. Please enter a valid SPARQL query.",
                            "errorCode": "PE99998",
                            "moreInfo": "Please contact the developer for more information.",
                        }
                for values in res:
                    results.append(dict(zip(res.vars, values)))
        return results
