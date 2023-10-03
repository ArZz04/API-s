import React from 'react';
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';

import Home from '../src/components/pages/homePage';
import Manage from './components/pages/managePage';
//import About from './components/About';
//import NotFound from './components/NotFound';

function App() {
  return (
    <Router>
      <div>
        <nav>
          <ul>
            <li>
              <Link to="/">Home</Link>
            </li>
            <li>
              <Link to="/about">About</Link>
            </li>
            <li>
              <Link to="/manage">Manage</Link>
            </li>
          </ul>
        </nav>

        <hr />

        <Routes>
          <Route exact path="/" component={Home} />
          <Route path="/about" component={Home} />
          <Route path="/manage" element={<Manage/>} />
          <Route component={Home} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;