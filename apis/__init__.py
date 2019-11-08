from flask_restplus import Api
from .rest_endpoints import api as rest_endpoints

api = Api(
    title='MWS_task',
    version='1.0.0',
    description='Bag of words implementation',
    prefix='/v1'
)

api.namespaces.clear()
api.add_namespace(rest_endpoints)