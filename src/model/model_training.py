# what-is-your-gender/src/model/model_training.py
import numpy as np
import tensorflow as tf
from sklearn.model_selection import train_test_split


# Load preprocessed data
data = np.load('../../dataset/combined_data.npy')
labels = np.load('../../dataset/combined_labels.npy')

# Convert labels to categorical (one-hot encoding)
labels = tf.keras.utils.to_categorical(labels)

# Split data into training and testing
from sklearn.model_selection import train_test_split
train_data, test_data, train_labels, test_labels = train_test_split(data, labels, test_size=0.2, random_state=42)

# Define the model for greyscale images
model = tf.keras.models.Sequential([
    tf.keras.layers.Conv2D(32, (3, 3), activation='relu', input_shape=(64, 64, 1)),  # Adjust for single-channel (greyscale)
    tf.keras.layers.MaxPooling2D(2, 2),
    tf.keras.layers.Conv2D(64, (3, 3), activation='relu'),
    tf.keras.layers.MaxPooling2D(2, 2),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(2, activation='softmax')  # 2 output neurons for 'Male' and 'Female'
])

# Compile the model
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Train the model
model.fit(train_data, train_labels, epochs=10, validation_data=(test_data, test_labels))

# Evaluate the model on the test set
test_loss, test_accuracy = model.evaluate(test_data, test_labels)

# Print the test loss and accuracy
print(f"Test Loss: {test_loss}")
print(f"Test Accuracy: {test_accuracy}")


# Save the model
model.save("./gender_model.keras")  # Adjusted path

