// src/components/TitleScreen.js
import React from 'react';
import './TitleScreen.css';

const TitleScreen = ({ onContinue }) => {
  return (
    <div className="title-screen">
      <h1>What Is Your Gender?</h1>
      <p>A Neural Network Gender Predictor</p>
      <p>Made by Sam Khoshnevis</p>
      <p>Trained with a Kaggle dataset</p>      
      <button onClick={onContinue}>Continue</button>
    </div>
  );
};

export default TitleScreen;
