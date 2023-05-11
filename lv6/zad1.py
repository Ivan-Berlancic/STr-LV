import numpy as np
from sklearn.datasets import fetch_openml
import joblib
import pickle
import matplotlib.pyplot as plt
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, confusion_matrix

X, y = fetch_openml('mnist_784', version=1, return_X_y=True, as_frame=False)

# TODO: prikazi nekoliko ulaznih slika

fig, axes = plt.subplots(3, 3, figsize=(8, 8))
axes = axes.ravel()
for i in np.arange(0, 9):
    axes[i].imshow(X[i].reshape(28, 28), cmap=plt.cm.gray)
    axes[i].axis('off')
    plt.subplots_adjust(hspace=0.5)
plt.show()

# skaliraj podatke, train/test split

X = X / 255.
X_train, X_test = X[:60000], X[60000:]
y_train, y_test = y[:60000], y[60000:]

# TODO: izgradite vlastitu mrezu pomocu sckitlearn MPLClassifier 

mlp_mnist = MLPClassifier(hidden_layer_sizes=(100,), max_iter=50, alpha=1e-4, solver='sgd', verbose=10, tol=1e-4, random_state=1, learning_rate_init=0.1)

mlp_mnist.fit(X_train, y_train)

# TODO: evaluirajte izgradenu mrezu

y_train_pred = mlp_mnist.predict(X_train)
train_acc = accuracy_score(y_train, y_train_pred)
print(f"Training accuracy: {train_acc:.3f}")
y_test_pred = mlp_mnist.predict(X_test)
test_acc = accuracy_score(y_test, y_test_pred)
print(f"Test accuracy: {test_acc:.3f}")

train_cm = confusion_matrix(y_train, y_train_pred)
test_cm = confusion_matrix(y_test, y_test_pred)
print("Confusion matrix for training set:\n", train_cm)
print("Confusion matrix for test set:\n", test_cm)

filename = "NN_model.sav"
joblib.dump(mlp_mnist, filename)

