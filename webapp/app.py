import flask as fl
import base64
import numpy as np

app = fl.Flask(__name__)


@app.route('/')
def home():
    #webpage.html used as the home page
    return app.send_static_file('webpage.html')


@app.route('/predictDigit', methods=['POST'])
def convertImage():

    # get the image from the request
    encodedImage = fl.request.values[('imgBase64')]
    decodedImage = base64.b64decode(encodedImage[22:])

    # save the image
    with open('image.png', 'wb') as f:
        f.write(decodedImage)

    return encodedImage

# Recommended to have this
if __name__ == "__main__":
    app.run(debug = True)