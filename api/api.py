
from io import BytesIO
from PIL import Image
from flask import Flask, send_file
from flask_restx import Resource, Api
from werkzeug.middleware.proxy_fix import ProxyFix

from api.utils import RandomImageFetcher

# Create the api
app = Flask(__name__, static_url_path='')
app.wsgi_app = ProxyFix(app.wsgi_app, x_proto=1, x_host=1)
api = Api(app)


@api.route('/<int:width>/<int:height>')
class ImageRoute(Resource):

    def get(self, width, height):

        # Retrieve an image of Alan Turing
        byte_image = RandomImageFetcher().download()

        # Open the image with PIL and resize it
        image = Image.open(BytesIO(byte_image))
        image = image.resize((width, height))

        # Save the image to a ByteIO container
        image_io = BytesIO()
        image.save(image_io, 'JPEG', quality=70)
        image_io.seek(0)

        # Serve the ByteIO image
        return send_file(image_io, mimetype='image/jpeg')
