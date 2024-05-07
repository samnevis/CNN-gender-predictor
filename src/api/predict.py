# what-is-your-gender/src/api/predict.py
from flask import Flask, request, jsonify
import numpy as np
import cv2
import tensorflow as tf
from PIL import Image
import io
import base64
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # This will enable CORS for all domains on all routes
try:
    model = tf.keras.models.load_model('what-is-your-gender/src/model/gender_model.keras')
    print("Model loaded successfully.")
except Exception as e:
    print(f"Error loading the model: {e}")

def preprocess_image(image, target_size):
    if image.mode != "L":
        image = image.convert("L")  
    image = image.resize(target_size)
    image = np.array(image)
    image = image / 255.0
    return image.reshape(-1, 64, 64, 1)

@app.route("/api/predict", methods=["POST"])
def predict():
    data = request.get_json(force=True)
    encoded = data["image"]
    decoded = base64.b64decode(encoded.split(",")[1])
    image = Image.open(io.BytesIO(decoded))
    processed_image = preprocess_image(image, target_size=(64, 64))
    
    prediction = model.predict(processed_image).tolist()

    return jsonify({"gender": int(prediction[0][0] > 0.5)})

if __name__ == "__main__":
    app.run(port=5000, debug=True)