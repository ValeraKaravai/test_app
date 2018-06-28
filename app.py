import base64
import os

from lib import Model
from flask import Flask, render_template, request
from flask_cors import CORS, cross_origin

app = Flask(__name__)
model = Model()
CORS(app, header=['Context-Type'])


@app.route('/', methods=["POST", "GET", "OPTIONS"])
def index_page():
    return render_template('index.html')


@app.route('/hook', methods=["POST", "GET", "OPTIONS"])
def get_image():
    if request.method == 'POST':
        image64 = request.values['imageBase64']
        draw_digit = request.values['digit']
        image_encoded = image64.split(',')[1]
        image = base64.decodebytes(image_encoded.encode('utf-8'))
        save = model.save_image(draw_digit, image)

        print('Done')
        return save



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
