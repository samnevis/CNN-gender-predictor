//src\components\AboutScreen.js
import React from 'react';
import './AboutScreen.css'; // Create and use this if you have specific styles for the about screen

const AboutScreen = () => {
    return (
      <div className="about-screen">
        <h1>About This App</h1>
        <p>This application uses neural networks to predict gender based on various parameters. It's designed to demonstrate the practical use of machine learning models in everyday applications.</p>
        <p>Developed by Sam Khoshnevis</p>
        <p>Data sourced from Kaggle datasets for training purposes.</p>
      </div>
    );
  };    

  export default AboutScreen;
