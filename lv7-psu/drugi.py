from tensorflow.keras.preprocessing.image import img_to_array
from keras.models import load_model
from matplotlib import pyplot as plt
from skimage.transform import resize
from skimage import color
import matplotlib.image as mpimg
import numpy as np

filename = 'test3.png'

img = mpimg.imread(filename)
img = color.rgb2gray(img)
img = resize(img, (28, 28))

plt.figure()
plt.imshow(img, cmap=plt.get_cmap('gray'))
plt.show()

img = img.reshape(1, 28, 28, 1)
img = img.astype('float32')

# Load the model
model = load_model("mnist_model.h5")

# Make prediction
prediction = model.predict(img)

# Get the predicted class label
predicted_class = np.argmax(prediction)

# Print the result
print("------------------------")
print("Predicted class:", predicted_class)
