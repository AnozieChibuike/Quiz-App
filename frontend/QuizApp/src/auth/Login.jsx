import { useEffect, useState } from "react";
import LoginForm from "../components/LoginForm";
import { useNavigate } from "react-router-dom";

const apiUrl = import.meta.env.VITE_API_URL;

function Login() {
  const navigate = useNavigate();
  useEffect(() => {
    document.title = "Login";
    const token = localStorage.getItem("token") || null;
    if (!!token) {
      console.log(token)
      navigate("/dashboard")
    };
    return () => {
      document.title = "QUIZ APP 2.0";
    };
  }, []);
  return (
    <>
      <h1 className="text-left max-sm:text-2xl max-md:text-3xl max-lg:text-4xl max-xl:text-5xl max-2xl:text-6xl text-4xl font-bold mt-40">
        Sign in to QUIZ APP 2.0
      </h1>
      <p className="text-left mb-12 mt-6">
        Get a magic link sent to your email address
      </p>
      <LoginForm />
    </>
  );
}

export default Login;
