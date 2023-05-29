import numpy as np
from tensorflow import keras
from tensorflow.keras import layers
from matplotlib import pyplot as plt
from sklearn.metrics import confusion_matrix

# Model / data parameters
num_classes = 10
input_shape = (28, 28, 1)

# train and test data
(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()

# Display some images from the training set
plt.figure(figsize=(10, 10))
for i in range(9):
    plt.subplot(3, 3, i + 1)
    plt.imshow(x_train[i], cmap="gray")
    plt.axis("off")
plt.show()

# Scale images to the range [0,1]
x_train_s = x_train.astype("float32") / 255
x_test_s = x_test.astype("float32") / 255

# Reshape images to (28, 28, 1)
x_train_s = np.expand_dims(x_train_s, -1)
x_test_s = np.expand_dims(x_test_s, -1)

print("x_train shape:", x_train_s.shape)
print(x_train_s.shape[0], "train samples")
print(x_test_s.shape[0], "test samples")

# Convert class labels to one-hot encoded vectors
y_train_s = keras.utils.to_categorical(y_train, num_classes)
y_test_s = keras.utils.to_categorical(y_test, num_classes)

# Create the model using keras.Sequential and show its structure
model = keras.Sequential(
    [
        keras.Input(shape=input_shape),
        layers.Conv2D(32, kernel_size=(3, 3), activation="relu"),
        layers.MaxPooling2D(pool_size=(2, 2)),
        layers.Conv2D(64, kernel_size=(3, 3), activation="relu"),
        layers.MaxPooling2D(pool_size=(2, 2)),
        layers.Flatten(),
        layers.Dropout(0.5),
        layers.Dense(num_classes, activation="softmax"),
    ]
)
model.summary()

# Define the training parameters using .compile()
model.compile(loss="categorical_crossentropy", optimizer="adam", metrics=["accuracy"])

# Train the model
batch_size = 128
epochs = 15
history = model.fit(x_train_s, y_train_s, batch_size=batch_size, epochs=epochs, validation_split=0.1)

# Evaluate the model on the training and test sets
train_loss, train_accuracy = model.evaluate(x_train_s, y_train_s, verbose=0)
test_loss, test_accuracy = model.evaluate(x_test_s, y_test_s, verbose=0)

print("Train accuracy:", train_accuracy)
print("Test accuracy:", test_accuracy)

# Generate predictions for the test set
y_pred = model.predict(x_test_s)
y_pred_classes = np.argmax(y_pred, axis=1)
y_true_classes = np.argmax(y_test_s, axis=1)

# Compute confusion matrices
train_confusion_matrix = confusion_matrix(np.argmax(y_train_s, axis=1), np.argmax(model.predict(x_train_s), axis=1))
test_confusion_matrix = confusion_matrix(y_true_classes, y_pred_classes)

# Plot confusion matrices
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(train_confusion_matrix, cmap="Blues")
plt.title("Train Confusion Matrix")
plt.colorbar()
plt.xlabel("Predicted Label")
plt.ylabel("True Label")

plt.subplot(1, 2, 2)
plt.imshow(test_confusion_matrix, cmap="Blues")
plt.title("Test Confusion Matrix")
plt.colorbar()
plt.xlabel("Predicted Label")
plt.ylabel("True Label")

plt.tight_layout()
plt.show()

# Save the model
model.save("mnist_model.h5")
