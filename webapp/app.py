import base64
import flask as fl
import cv2

from PIL import Image, ImageOps

app = fl.Flask(__name__)

height = 28
width = 28
size = height, width

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

    # ANTIALIAS removes the "stair-step" look
    userImage = Image.open("image.png")

    newImage = ImageOps.fit(userImage, size, Image.ANTIALIAS)


    return encodedImage

# Recommended to have this
if __name__ == "__main__":
    app.run(debug = True)