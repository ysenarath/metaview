from flask import Flask

from knet import api, views
from knet.config import CONFIG

app = Flask(__name__)

app.register_blueprint(api.bp, url_prefix='/api/v%0.1f' % (CONFIG['API_INFO']['version']))
app.register_blueprint(views.bp, url_prefix='/')

if __name__ == '__main__':
    app.run(debug=True)
