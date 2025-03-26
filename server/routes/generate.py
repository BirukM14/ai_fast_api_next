from fastapi import APIRouter
from models.request_model import GenerateRequest
from services.generator import process_input

router = APIRouter(prefix="/generate", tags=["Generate"])

@router.post("/")
async def generate_response(request: GenerateRequest):
    response_message = process_input(request.input)
    return {"message": response_message}
