import os

CONFIG = dict()

# App
CONFIG['APP_TITLE'] = 'KnowledgeNet'

# Path
CONFIG['PROJECT_DIR'] = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
CONFIG['RDF_PATH'] = os.path.join(CONFIG['PROJECT_DIR'], 'resources', 'graph.rdf.json')

# API
CONFIG['API_INFO'] = {
    '@context': 'http://schema.org/',
    '@type': 'WebAPI',
    'name': 'KnowledgeNet Development API',
    'description': 'The KnowledgeNet Development API lets you find and create entities in the KnowledgeNet Graph.',
    'documentation': 'https://www.docs.knet.org',
    'version': 0.1,
}
