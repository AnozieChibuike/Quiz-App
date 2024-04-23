import React from "react";
import { Route, Routes } from "react-router-dom";
import Login from "./auth/Login";
import NoPage from "./NoPage";
import "./App.css";
import VerifyToken from "./auth/VerifyToken";
import SignUp from "./auth/SignUp";


function App() {
  return (
    <Routes>
      <Route path="login" element={<Login />} />
      <Route path="/verify" element={<VerifyToken />} />
      <Route path="/createprofile" element={<SignUp />} />
      <Route path="*" element={<NoPage />} />
    </Routes>
  );
}

export default App;
