# what-is-your-gender\src\data_preparation\preprocess_step_2.py
import cv2
import numpy as np
import os
import glob

# Define paths
base_path = 'c:/Users/samne/gender app/what-is-your-gender/src/data_preparation/dataset'
male_path = os.path.join(base_path, 'new male/*.jpeg')
female_path = os.path.join(base_path, 'new female/*.jpeg')

# Define the target dimensions
target_size = (64, 64)  # Example size, adjust as needed

def preprocess_images(image_paths, label):
    data = []
    labels = []
    for img_path in glob.glob(image_paths):
        # Read the image
        img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
        if img is not None:
            # Resize the image
            img = cv2.resize(img, target_size)
            # Normalize the pixel values
            img = img / 255.0
            data.append(img)
            labels.append(label)
    return data, labels

# Process images
male_data, male_labels = preprocess_images(male_path, label=0)  # Assuming 0 for male
female_data, female_labels = preprocess_images(female_path, label=1)  # Assuming 1 for female

# Convert lists to NumPy arrays
male_data = np.array(male_data)
female_data = np.array(female_data)
male_labels = np.array(male_labels)
female_labels = np.array(female_labels)

# Example: view the shape of the arrays
print("Male data shape:", male_data.shape)
print("Female data shape:", female_data.shape)

# Combine male and female data into one dataset
combined_data = np.concatenate((male_data, female_data), axis=0)
combined_labels = np.concatenate((male_labels, female_labels), axis=0)

# Save combined dataset
try:
    np.save('c:/Users/samne/gender app/what-is-your-gender/src/data_preparation/dataset/combined_data.npy', combined_data)
    np.save('c:/Users/samne/gender app/what-is-your-gender/src/data_preparation/dataset/combined_labels.npy', combined_labels)
    print("Files saved successfully.")
except Exception as e:
    print(f"Failed to save files: {e}")

