import json
from apistar import App, Route

mydataDummy = {
    'lugar': 'medellin',
    'magnitud': '3.5'

}


def welcome(name=None):
    if name is None:
        return {'message': 'Welcome to API Star!'}
    return {'message': 'Welcome to API Star, %s!' % name}

def api():
    data = mydataDummy
    return data
    


routes = [
    Route('/', method='GET', handler=welcome),
    Route('/api', method='GET', handler=api),
]

app = App(routes=routes)


if __name__ == '__main__':
    app.serve('127.0.0.1', 5000, debug=True)