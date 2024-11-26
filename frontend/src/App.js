// frontend/src/App.js

import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Dashboard from './components/Dashboard';
import FlightDetails from './components/FlightDetails';

function App() {
  return (
    <Router>
      <div className="App">
        <Routes>
          <Route path="/" element={<Dashboard />} />
          <Route path="/flight/:flightId" element={<FlightDetails />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
