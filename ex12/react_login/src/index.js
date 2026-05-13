import React from 'react';
import ReactDOM from 'react-dom/client'; // 注意這裡多了一個 /client
import './index.css';
import App from './App';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);