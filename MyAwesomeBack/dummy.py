import json
from apistar import App, Route
from apistar import http

import os

BASE_DIR = os.path.dirname(__file__)
TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')
STATIC_DIR = os.path.join(BASE_DIR, 'static')

mydataDummy = {
    'lugar': 'medellin',
    'magnitud': '3.5'

}


def welcome(app: App, name=None):
    return app.render_template('index.html', name=name)

def api():
    #content = mydataDummy
    #headers = {'Content-Type': 'text/plain'}
    #return http.Response(content, headers=headers)
    data = mydataDummy
    return data
    


routes = [
    Route('/', method='GET', handler=welcome),
    Route('/api', method='GET', handler=api),
]

app = App(routes=routes, template_dir=TEMPLATE_DIR, static_dir=STATIC_DIR)


if __name__ == '__main__':
    app.serve('0.0.0.0', 5000, debug=True)
