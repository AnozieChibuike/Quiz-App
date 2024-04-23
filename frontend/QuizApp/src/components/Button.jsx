import React from "react";
import { FaSpinner } from 'react-icons/fa';

function Button({ children, onClick, className, disabled }) {
  return (
    <button
      onClick={onClick}
      className={`bg-blue-700 ${
        !disabled ? "cursor-pointer" : "cursor-default"
      }  ${
        !disabled ? "hover:bg-blue-500" : ""
      } text-white font-bold w-full py-2 px-4 rounded ${className}`}
      disabled={disabled}
    >
      {disabled ? (<FaSpinner className="animate-spin text-2xl text-white" />) : children}
    </button>
  );
}

export default Button;
