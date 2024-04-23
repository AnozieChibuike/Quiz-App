import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";

const apiUrl = import.meta.env.VITE_API_URL;

function VerifyToken() {
  const navigate = useNavigate();

  useEffect(() => {
    const searchParams = new URLSearchParams(window.location.search);
    const token = searchParams.get("token");
    verifyToken(token);
  }, []);
  async function verifyToken(token) {
    try {
      const response = await fetch(`${apiUrl}/magic_link/verify?${token}`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ token }),
      });
      const data = await response.json();
      if (response.status === 404) {
        navigate("/createprofile", {
          state: { email: data.email },
        }); 
        return
      } 
      if (!response.ok) {
        navigate("/login", {
          state: { error: data?.error || data?.reason == "code expired" ? "The token has expired, Please request a new one" : data?.reason  || "Uh-oh something went wrrong" },
          replace: true,
        })
        return
      }
      localStorage.setItem("token", data.token);
      navigate("/dashboard", {
          state: { token: data.token },
        }); 
        return
    } catch (error) {
      console.error(error);
    }
  }

  return ;
}

export default VerifyToken;
