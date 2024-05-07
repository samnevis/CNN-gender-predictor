# what-is-your-gender\src\data_preparation\preprocess_step_1.py
import os
from PIL import Image

def convert_images(source_dir, target_dir):
    # Create target directory if it doesn't exist
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)

    # Initialize a counter for unique naming
    counter = 1
    
    # Loop through all files in the source directory
    for filename in os.listdir(source_dir):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):  # Check for image files
            # Construct full file path
            file_path = os.path.join(source_dir, filename)
            # Open the image
            with Image.open(file_path) as img:
                # Convert image to RGB mode if it is not
                if img.mode != 'RGB':
                    img = img.convert('RGB')
                # Define new filename
                new_filename = f"{counter}.jpeg"
                new_file_path = os.path.join(target_dir, new_filename)
                # Save the image in JPEG format
                img.save(new_file_path, 'JPEG')
                print(f"Saved {new_file_path}")
                # Increment the counter
                counter += 1

# Specify the source and target directories
source_directory = 'path_to_your_source_directory'
target_directory = 'path_to_your_target_directory'

# Call the function
convert_images(source_directory, target_directory)
