"use client"; // Required because it's a client component

import { useState } from "react";

export default function InputForm() {
    const [inputValue, setInputValue] = useState("");
    const [response, setResponse] = useState("");

    const handleSubmit = async () => {
        try {
            const res = await fetch("/api/generate", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ input: inputValue }),
            });

            const data = await res.json();
            setResponse(data.message || "Response received!");
        } catch (error) {
            console.error("Error:", error);
            setResponse("Failed to fetch response.");
        }
    };

    return (
        <div className="flex justify-between p-4 border rounded-lg shadow-md">
            <input
                type="text"
                value={inputValue}
                onChange={(e) => setInputValue(e.target.value)}
                placeholder="Enter something..."
                className="border p-2 rounded-md w-full"
            />
           
            <button
                onClick={handleSubmit}
                className="mt-2 bg-gray-500 hover:white text-white px-4 py-2 rounded-md"
            >
                Submit
            </button>
            {response && <p className="mt-2 text-green-600">{response}</p>}
        </div>
    );
}
