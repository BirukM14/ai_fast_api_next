from pydantic import BaseModel

# Model for text generation requests
class TextRequest(BaseModel):
    prompt: str
