"use client"; // Required for client-side components

import { useState } from "react";

export default function InputForm() {
    const [inputValue, setInputValue] = useState("");
    const [response, setResponse] = useState("");

    const handleSubmit = async () => {
        try {
            const res = await fetch("/api/generate", {  // Fixed fetch URL
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ prompt: inputValue }),  // Updated key name
            });

            if (!res.ok) {
                throw new Error("Failed to fetch response.");
            }

            const data = await res.json();
            setResponse(data.generated_text );
        } catch (error) {
            console.error("Error:", error);
            setResponse("Failed to fetch response.");
        }
    };

    return (
        <div className="flex flex-col gap-2 p-4 border rounded-lg shadow-md w-96">
            <input
                type="text"
                value={inputValue}
                onChange={(e) => setInputValue(e.target.value)}
                placeholder="Enter a prompt..."
                className="border p-2 rounded-md w-full"
            />
           
            <button
                onClick={handleSubmit}
                className="bg-blue-500 hover:bg-blue-600 text-white px-4 py-2 rounded-md transition"
            >
                Submit
            </button>

            {response && <p className="text-green-600">{response}</p>}
        </div>
    );
}
