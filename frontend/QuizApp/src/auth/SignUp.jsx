import { useEffect, useState } from "react";
import SignUpForm from "../components/SignUpForm";
import { useNavigate, useLocation } from "react-router-dom";

const apiUrl = import.meta.env.VITE_API_URL;

function SignUp() {
  const navigate = useNavigate();
  const location = useLocation();
  useEffect(() => {
    document.title = "Sign Up";
    const email = location.state?.email;
    if (!email) {
      navigate("/login");
    }
    return () => {
      document.title = "QUIZ APP 2.0";
    };
  }, []);
  return (
    <>
      <h1 className="text-left max-sm:text-1xl max-md:text-2xl max-lg:text-3xl max-xl:text-4xl max-2xl:text-5xl text-3xl font-bold mb-20">
        Complete your Profile
      </h1>
      <SignUpForm />
    </>
  );
}

export default SignUp;
