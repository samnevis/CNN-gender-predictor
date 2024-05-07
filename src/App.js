// src/App.js
import React, { useState } from 'react';
import './App.css';
import TitleScreen from './components/TitleScreen';
import UploadScreen from './components/UploadScreen'; // You will create this component next

function App() {
  const [screen, setScreen] = useState('title'); // 'title' or 'upload'

  return (
    <div className="App">
      {screen === 'title' ? (
        <TitleScreen onContinue={() => setScreen('upload')} />
      ) : (
        <UploadScreen />
      )}
    </div>
  );
}

export default App;
