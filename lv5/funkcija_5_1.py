from sklearn import datasets
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from scipy.cluster.hierarchy import dendrogram, linkage


def generate_data(n_samples, flagc):
    
    if flagc == 1:
        random_state = 365
        X,y = datasets.make_blobs(n_samples=n_samples, random_state=random_state)
        
    elif flagc == 2:
        random_state = 148
        X,y = datasets.make_blobs(n_samples=n_samples, random_state=random_state)
        transformation = [[0.60834549, -0.63667341], [-0.40887718, 0.85253229]]
        X = np.dot(X, transformation)
        
    elif flagc == 3:
        random_state = 148
        X, y = datasets.make_blobs(n_samples=n_samples,
                                    centers=4,
                                    cluster_std=[1.0, 2.5, 0.5, 3.0],
                                    random_state=random_state)

    elif flagc == 4:
        X, y = datasets.make_circles(n_samples=n_samples, factor=.5, noise=.05)
        
    elif flagc == 5:
        X, y = datasets.make_moons(n_samples=n_samples, noise=.05)
    
    else:
        X = []
        
    return X

X = generate_data(500, 1)

kmeans = KMeans(n_clusters=3)
kmeans.fit(X)

labels = kmeans.predict(X)
centers = kmeans.cluster_centers_

plt.scatter(X[:,0], X[:,1], c=labels)
plt.scatter(centers[:,0], centers[:,1], marker='x', s=200, linewidths=3, color='r')
plt.show()

inertia = []

for k in range(2, 21):
    kmeans = KMeans(n_clusters=k)
    kmeans.fit(X)
    inertia.append(kmeans.inertia_)

plt.plot(range(2, 21), inertia, marker='o')
plt.xticks(range(3, 21, 3))
plt.xlabel('Broj klastera')
plt.ylabel('Vrijednost kriterijske funkcije')
plt.show()

X = generate_data(50, 1)

Z = linkage(X, method='complete')

plt.figure(figsize=(25, 10))
dendrogram(Z)
plt.show()
