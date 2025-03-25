from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from model import generate_text
import uvicorn

app = FastAPI()

# Request body model
class TextRequest(BaseModel):
    prompt: str

# Root route
@app.get("/bura")
def read_root():
    return {"message": "Welcome to the AI Content Generator API!"}

# AI content generation endpoint
@app.post("/generate")
def generate_content(request: TextRequest):
    try:
        result = generate_text(request.prompt)
        return {"generated_text": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Run server
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
