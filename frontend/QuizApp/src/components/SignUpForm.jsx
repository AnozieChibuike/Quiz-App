import React, { useEffect, useState } from "react";
import InputWithError from "./InputWithError";
import Button from "./Button";
import { MdArrowForward } from "react-icons/md";
import { useLocation, } from "react-router-dom";

const apiUrl = import.meta.env.VITE_API_URL;

function SignUpForm() {
  const [apiError, setApiError] = useState("");
  const location = useLocation();
  const [UserData, setUserData] = useState({
    email: "",
    username: "",
    fullname: "",
    phone: "",
    is_admin: false,
  });
  const [error, setErrors] = useState({});
  const [loading, setLoading] = useState(false);
  useEffect(() => {
    if (location.state?.email) {
      setUserData((prevState) => ({
        ...prevState,
        email: location.state.email,
      }));
    } else {
      return;
    }
  }, []);

  const createprofile = async () => {
    setLoading(true);
    try {
      const response = await fetch(apiUrl + "/user", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ action: "create", ...UserData }),
      });
      const data = await response.json();
      console.log(data);
      if (!response.ok) {
        if (typeof data.error === "string") {
          setApiError(data.error)
          return;
        }
        Object.keys(data.error).forEach((key) => {
            handleError(data.error[key][0], key);
        })
        return;
      }
      localStorage.setItem("token", data.token);
      window.open("/login", "_blank");
      return
    } catch (error) {
      console.log(error);
      return;
    } finally {
      setLoading(false);
    }
  };

  const handleChange = (text, input) => {
    setUserData((prevState) => ({ ...prevState, [input]: text }));
  };
  const handleError = (error, input) => {
    setErrors((prevState) => ({ ...prevState, [input]: error }));
  };

  const validate = async () => {
    let isValid = true;
    if (!UserData.email) {
      isValid = false;
      handleError("Email is required", "email");
    } else if (!UserData.email.match(/\S+@\S+\.\S+/)) {
      isValid = false;
      handleError("Please input a valid email", "email");
    }
    if (!UserData.username) {
      isValid = false;
      handleError("Username is required", "username");
    }
    if (!UserData.fullname) {
      isValid = false;
      handleError("Fullname is required", "fullname");
    }
    if (!UserData.phone) {
      isValid = false;
      handleError("Phone Number cannot be empty", "phone");
    }
    if (isValid) createprofile();
  };
  return (
    <div>
      <InputWithError
        label="Fullname"
        value={UserData.fullname}
        onChange={(e) => handleChange(e.target.value, "fullname")}
        placeholder="John Doe"
        error={error.fullname}
        onFocus={() => handleError(null, "fullname")}
      />

      <InputWithError
        label="Username"
        value={UserData.username}
        onChange={(e) => handleChange(e.target.value, "username")}
        placeholder="Educationist3201"
        error={error.username}
        onFocus={() => handleError(null, "username")}
      />

      <InputWithError
        label="Email address"
        value={UserData.email}
        onChange={(e) => handleChange(e.target.value, "email")}
        placeholder="example@mail.com"
        disabled={true}
        error={error.email}
        onFocus={() => handleError(null, "email")}
      />

      <InputWithError
        label="Phone Number"
        value={UserData.phone}
        onChange={(e) => handleChange(e.target.value, "phone")}
        placeholder="08012345678"
        error={error.phone}
        onFocus={() => handleError(null, "phone")}
      />
      <Button
        className="flex items-center justify-center"
        onClick={validate}
        disabled={loading}
      >
        <div className="flex items-center">
          Sign up <MdArrowForward style={{ verticalAlign: "middle" }} />
        </div>
        <div></div>
      </Button>
      {!!apiError && <p className="text-red-500 text-xs italic text-left">{apiError}</p>}
    </div>
  );
}

export default SignUpForm;
