import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";

import "./App.css";
import Home from "./pages/Home";
import UserLogin from "./pages/UserLogin";
import Register from "./pages/Register";
import DoctorLogin from "./pages/DoctorLogin";

const App = () => {
  return (
    <div>
      <Router>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/UserLogin" element={<UserLogin />} />
          <Route path="/DoctorLogin" element={<DoctorLogin />} />
          <Route path="/Register" element={<Register />} />
        </Routes>
      </Router>
    </div>
  );
};

export default App;
