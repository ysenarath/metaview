import os

from rdflib import Graph


class GraphReader(object):
    def __init__(self, fp):
        self.fp = fp
        self.graph = None
        self._file_not_exist()

    def __enter__(self) -> Graph:
        with open(self.fp, 'r', encoding='utf-8') as f:
            self.graph = Graph().parse(data=f.read(), format='json-ld')
        return self.graph

    def __exit__(self, exc_type, exc_val, exc_tb):
        assert self.graph is not None, 'Initialize the variable \'graph\' before trying to exit the procedure.'
        with open(self.fp, 'w', encoding='utf-8') as fp:
            context = self.graph.serialize(format='json-ld', indent=4).decode('utf-8')
            fp.write(context)
        self.graph.close()

    def _file_not_exist(self):
        if not os.path.exists(self.fp):
            with open(self.fp, 'w', encoding='utf-8') as fp:
                fp.write(str([]))


def open_graph(fp) -> GraphReader:
    return GraphReader(fp)
