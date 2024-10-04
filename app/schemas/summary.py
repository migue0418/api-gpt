from pydantic import BaseModel
from app.utils.gpt_models import GPTModel


class SummaryRequest(BaseModel):
    text: str
    model: GPTModel = GPTModel.GPT_4


class SummaryResponse(BaseModel):
    summary: str
