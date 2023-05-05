# -*- coding: utf-8 -*-
"""
Created on Sun Dec 02 12:08:00 2018

@author: Grbic
"""

import scipy as sp
from sklearn import cluster, datasets
import numpy as np
import matplotlib.pyplot as plt

import matplotlib.image as mpimg

imageNew = mpimg.imread('example_grayscale.png')
imageNew = mpimg.imread('example.png')

X = imageNew.reshape(-1, 3)

try:
 face = sp.face(gray=True)
except AttributeError:
 from scipy import misc
 face = misc.face(gray=True)

X = imageNew.reshape((-1, 1))

k_means = cluster.KMeans(n_clusters=3, n_init=1)
k_means.fit(X)
values = k_means.cluster_centers_.squeeze()
labels = k_means.labels_
image_compressed = np.choose(labels, values)
image_compressed.shape = imageNew.shape

plt.figure(1)
plt.imshow(imageNew, cmap='gray')
plt.show()

plt.figure(2)
plt.imshow(image_compressed, cmap='gray')
plt.show()