import React from "react";
import { useNavigate } from "react-router-dom";

const Home = (props) => {
  const navigate = useNavigate();

  return (
    <>
      <h1>Welcome to Remote patient Monitoring portal </h1>
      <p>
        <button onClick={() => navigate("/UserLogin")}>UserLogin</button>
      </p>
      <p>
        <button onClick={() => navigate("/DoctorLogin")}>DoctorLogin</button>
      </p>

    </>
  );
};

export default Home;