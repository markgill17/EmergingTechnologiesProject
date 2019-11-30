import base64
import flask as fl
import cv2
import numpy as np

from PIL import Image, ImageOps
from flask import render_template

from keras.models import load_model
model = load_model('../model.h5')

app = fl.Flask(__name__)

height = 28
width = 28
size = height, width

@app.route('/')
def home():
    # webpage.html used as the home page
    return render_template('webpage.html')


@app.route('/predictDigit', methods=['POST'])
def convertImage():

    # get the image from the request
    encodedImage = fl.request.values[('imgBase64')]
    decodedImage = base64.b64decode(encodedImage[22:])

    # save the image
    with open('image.png', 'wb') as f:
        f.write(decodedImage)

    # open the created image
    createdImage = Image.open("image.png")

    # ANTIALIAS removes the "stair-step" look
    newImage = ImageOps.fit(createdImage, size, Image.ANTIALIAS)

    # saving resized image (28x28)
    newImage.save("imageCropped.png")

    # loading newly shaped
    cv2Img = cv2.imread("imageCropped.png")

    # converting to greyscale and reshaping
    grayScaleImg = cv2.cvtColor(cv2Img, cv2.COLOR_BGR2GRAY)
    grayScaleArr = np.array(grayScaleImg).reshape(1, 784) #28x28

    # using our model that we saved and imported to run our saved, cropped image.
    setPrediction = model.predict(grayScaleArr)
    getPrediction = np.array(setPrediction[0])

    # returning our predicted digit as a string to display
    predictedDigit = str(np.argmax(getPrediction))
    print(predictedDigit)

    return predictedDigit

# Recommended to have this
if __name__ == "__main__":
    app.run(debug = True)

