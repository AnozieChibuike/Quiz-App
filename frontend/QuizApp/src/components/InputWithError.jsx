import React from 'react';

function InputWithError({ label, value, onChange, error, placeholder, ...props }) {
    return (
        <div className="mb-4">
            <label className="block text-gray-700 text-sm font-bold mb-2 text-left">
                {label}
            </label>
            <input
                type="text"
                value={value}
                onChange={onChange}
                placeholder={placeholder}
                className={`shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline ${error ? 'border-red-500' : 'border-gray-300'}`}
                disabled={props.disabled}
                {...props}
            />
            {error && <p className="text-red-500 text-xs italic text-left">{error}</p>}
        </div>
    );
}

export default InputWithError;
