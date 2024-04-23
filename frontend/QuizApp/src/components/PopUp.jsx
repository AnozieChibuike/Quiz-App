import React from 'react';

const PopUp = ({ message, type, onClose }) => {
  // Determine the color of the popup based on the message type
  const bgColor = type === 'success' ? 'bg-blue-700' : 'bg-red-500';

  return (
    <div className={`fixed inset-0 flex items-center justify-center p-4 bg-white text-white`}>
      <div className={`max-w-sm shadow-lg rounded-lg p-4 ${bgColor}`}>
        <div className="flex justify-center flex-col items-center py-4">
          <h1 className='font-bold '>Magic Link Sent </h1>
          <span className='m-3'>Please Check your Email</span>
          
        </div>
      </div>
    </div>
  );
};

export default PopUp;
