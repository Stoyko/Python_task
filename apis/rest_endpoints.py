from flask_restplus import Namespace, Resource

from application.bag_of_words import BagOfWords
from application.load_data import LoadData

api = Namespace('bow', description='Bag of Words')
load_data = LoadData()
bag_of_words = BagOfWords(loaded_data=load_data)




@api.route('/<record_id>')
@api.param(name='record_id')
class RecordID(Resource):

    @api.doc('Get bag of words vector')
    def get(self, record_id):
        """Returns a bag of word vector of the title for the requested record ID
            The length of the vector is based on all the words in the bag.
            <br>
            <h3> Example Request: </h3>
            <pre> curl -X GET "http://127.0.0.1:8000/v1/bow/(Uk)vdc_100029455301.0x000001" -H "accept: application/json" </pre>
            <br>
            <b> Result: </b>
            <pre> {"bag_of_words_vector": [
            0,
            2,
            0,
            0,
            1,
            0,
            0
            ]}</pre>
            <br>"""
        vector = bag_of_words.get_bag_of_words_vector(record_id=record_id)
        if vector:
            return {'bag_of_words_vector': vector}, 200
        else:
            return {'status_code': 204, 'message': 'Not Found'}, 204
