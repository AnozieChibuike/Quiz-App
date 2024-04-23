import React, { useEffect, useState } from "react";
import InputWithError from "./InputWithError";
import Button from "./Button";
import { FaEnvelope } from "react-icons/fa";
import { MdArrowForward } from "react-icons/md";
import { useLocation } from "react-router-dom";
import PopUp from "./PopUp";

const apiUrl = import.meta.env.VITE_API_URL;

function LoginForm() {
  const location = useLocation();
  const [email, setEmail] = useState("");
  const [emailError, setEmailError] = useState("");
  const [loading, setLoading] = useState(false);
  const [showPopup, setShowPopup] = useState(false);
  const [popupType, setPopupType] = useState('success');
  const [message, setMessage] = useState('');

  const handleShowPopup = (type, msg) => {
    setPopupType(type);
    setMessage(msg);
    setShowPopup(true);
  };

  useEffect(() => {
    if (performance.navigation.type === performance.navigation.TYPE_RELOAD) {
      setEmailError(null);
    } else {
      setEmailError(location.state?.error);
    }
  }, [location.state]);


  const handleSubmit = async (event) => {
    if (emailError) return
    setLoading(true);
    try {
      event.preventDefault();
      const isValid = await validateEmail();
      if (isValid) await magicLink();
      else return;
    } catch (error) {
    } finally {
      setLoading(false);
    }
  };

  const magicLink = async () => {
    try {
      const response = await fetch(apiUrl + "/magic_link", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ email }),
      });
      const data = await response.json();
      if (!response.ok) {
        setEmailError(data.message.email[0] || "Request could not be sent");
        return;
      }
      handleShowPopup('success', data.message)
    } catch (error) {
      setEmailError(error.message || "Request could not be sent");
    }
  };

  const validateEmail = async () => {
    let isValid = false;
    if (!email) {
      setEmailError("Please input email");
      return isValid;
    } else if (!email.match(/\S+@\S+\.\S+/)) {
      setEmailError("Please input a valid email");
      return isValid;
    }
    isValid = true;
    return isValid;
  };
  return (
    <div>
      <InputWithError
        label="Email address"
        value={email}
        onChange={(e) => setEmail(e.target.value)}
        placeholder="example@mail.com"
        error={emailError}
        onFocus={() => setEmailError("")}
      />
      <Button
        className={`flex items-center ${
          loading ? "justify-center" : "justify-between"
        }`}
        onClick={handleSubmit}
        disabled={loading}
      >
        <FaEnvelope className="" />
        <div className="flex items-center">
          Get Magic Link <MdArrowForward style={{ verticalAlign: "middle" }} />
        </div>
        <div></div>
      </Button>
      {showPopup && <PopUp type={popupType} message={message} onClose={() => setShowPopup(false)} />}
    </div>
  );
}

export default LoginForm;
