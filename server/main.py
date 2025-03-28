from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from models.model import generate_text
from pydantic import BaseModel
import uvicorn
from models.request_model import TextRequest

 # Ensure this function exists

app = FastAPI()


# Enable CORS for frontend requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Replace with ["http://localhost:3000"] for security
    allow_credentials=True,
    allow_methods=["POST"],  # Fixed typo
    allow_headers=["*"],  # Fixed empty list
)
# Root route
@app.get("/")
def read_root():
    return {"message": "Welcome to the AI Content Generator API!"}

# AI content generation endpoint
@app.post("/generate")
def generate_content(request: TextRequest):
    
    try:
        result = generate_text(request.prompt)
        print(result)
        return {"generated_text": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Run server
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
