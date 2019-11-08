from flask import Flask
from apis import api

app = Flask(__name__)
# app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
api.init_app(app)


if __name__ == '__main__':
    app.run(port=8000)





