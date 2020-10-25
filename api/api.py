
from io import BytesIO
from PIL import Image
from flask import Flask
from flask_restx import Resource, Api

from api.utils import RandomImageFetcher

# Create the api
app = Flask(__name__)
api = Api(app)


@api.route('/<int:width>/<int:height>')
class Image(Resource):

    def get(self, width, height):

        # Retrieve an image of Alan Turing
        byte_image = RandomImageFetcher().download()

        # Open the image with PIL and resize it
        image = Image.open(BytesIO(byte_image))
        image.resize((width, height))

        # Return the image
        return {todo_id: todos[todo_id]}
