# what-is-your-gender/src/model/model_training.py
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
from tensorflow.keras.utils import to_categorical
from sklearn.model_selection import train_test_split


# Load preprocessed data
data = np.load('what-is-your-gender/src/data_preparation/dataset/combined_data.npy')
labels = np.load('what-is-your-gender/src/data_preparation/dataset/combined_labels.npy')

# Convert labels to categorical (one-hot encoding)
labels = to_categorical(labels)

# Split data into training and testing
from sklearn.model_selection import train_test_split
train_data, test_data, train_labels, test_labels = train_test_split(data, labels, test_size=0.2, random_state=42)

# Define the model for greyscale images
model = Sequential([
    Conv2D(32, (3, 3), activation='relu', input_shape=(64, 64, 1)),  # Adjust for single-channel (greyscale)
    MaxPooling2D(2, 2),
    Conv2D(64, (3, 3), activation='relu'),
    MaxPooling2D(2, 2),
    Flatten(),
    Dense(128, activation='relu'),
    Dense(2, activation='softmax')  # 2 output neurons for 'Male' and 'Female'
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
model.save('what-is-your-gender/src/model/gender_model.keras')  # Adjusted path
