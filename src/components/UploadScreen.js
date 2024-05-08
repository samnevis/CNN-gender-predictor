// src/components/UploadScreen.js
import React, { useState } from 'react';
import './UploadScreen.css';

const UploadScreen = () => {
    const [image, setImage] = useState(null); // State to store the uploaded image
    const [prediction, setPrediction] = useState(null); // State to store the prediction result

    const handleUpload = (event) => {
        const file = event.target.files[0];
        if (file && file.type.startsWith('image/')) {
            const reader = new FileReader();
            reader.onloadend = async () => {
                setImage(reader.result);
                await predictGender(reader.result);
            };
            reader.readAsDataURL(file);
        } else {
            alert('Please upload an image file.');
        }
    };

    const predictGender = async (imageData) => {
      try {
          const response = await fetch('http://127.0.0.1:5000/api/predict', {
            method: 'POST',
            mode: 'no-cors',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ image: imageData }),
          });
  
          if (!response.ok) {
              throw new Error('Failed to fetch data from server.');
          }
  
          const result = await response.json();
          setPrediction(result.gender);
      } catch (error) {
          alert('An error occurred while fetching data from server: ' + error.message);
      }
    };
  

    return (
        <div className="upload-screen">
            <input type="file" onChange={handleUpload} />
            {image && <img src={image} alt="Uploaded" style={{ marginTop: '20px', maxWidth: '40%', maxHeight: '40%' }} />}
            {prediction && <p>Predicted Gender: {prediction === 1 ? 'Female' : 'Male'}</p>}
        </div>
    );
};

export default UploadScreen;

