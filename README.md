# EmergingTechnologiesProject

## Intro
This project is part of my 4th year Software Development module in GMIT, Emerging Technologies. It uses a neural network, trained with the MNIST dataset, to recognise hand-drawn digits from the user. The hand-drawn digits are sent to the model from a canvas on a flask app. The model was coded in python using the Keras library in a Jupyter Notebook. My IDE of choice was PyCharm. The web app is an amalgamation of HTML, JavaScript and CSS. This is connected to my model through a flask server.

## Research
### Jupyter
"The Jupyter Notebook is an open-source web application that allows you to create and share documents that contain live code, equations, visualizations and narrative text." Via: https://jupyter.org.
It supports over 40 languages and integrates very well with GitHub.

### TensorFlow
TensorFlow is an open-source machine learning tool. It helps you build models, like I have for this project, using the Keras API. It enables you to deploy your model easily.

### Keras
"Keras is a high-level neural networks API, written in Python and capable of running on top of TensorFlow, CNTK, or Theano." Via: https://keras.io/.
Keras is a deep learning library used on top TensorFlow. It keeeps it's APIs simple and consistent and it keeps controls augmented for easy use of standard controls. It also tends be easy to run for a CPU or GPU.

### MNIST
The MNIST database (Modified National Institute of Standards and Technology database) is a database of hand-written digits. It's used to train neural networks and is commonly used in machine learning. The images from the MNIST dataset were normalized to fit 28x28 pixel bounding and converted to greyscale. Via: https://en.wikipedia.org/wiki/MNIST_database

### PIL
PIL(Python Image Library) is also known as Pillow. It is a free library that supports opening, manipulating and saving many different image file formats. Via: https://en.wikipedia.org/wiki/Python_Imaging_Library.
In my project, I use the Image function to open the image. I also used the ImageOps function to reshape the image.

### OpenCV
OpenCV is a library commonly used for machine learning and computer vision. It can be used to find edges of objects or identify human faces using machine learning. I used it to convert my image that I would pass through my model to greyscale. This yeilded better results.

## How to run
* Git clone ```https://github.com/markgill17/EmergingTechnologiesProject```
* Using the command line, navigate to the project directory and then into the ```webapp``` folder.
* Enter command ```python webapp.py``` to run.
* Enter ```http://127.0.0.1:5000/``` into the searchbar of your internet browser of choice.
* Carefully draw a number in the 0-9 range in the canvas.
* Hit the Save button. This will hopefully predict the digit you have drawn.
* To try again, hit the Clear button to clear the canvas.

## Environment
To use run this project, you may need:
* Anaconda. Preferably version 3.7 or later. You can get it here: https://www.anaconda.com/distribution/. If you already have a version installed that is too old, run ```conda update --all``` to get the latest version.
* Keras and TensorFlow. Run ```conda install -c conda-forge keras tensorflow``` from a terminal after you install Anaconda.
* OpenCV. Run ```pip install opencv-python``` from a terminal.
* Run ```pip install requirements.txt``` to install my comprehensive list.
