from fastapi import APIRouter, HTTPException
from app.schemas.summary import SummaryRequest, SummaryResponse
from app.external_services.gpt_service import generate_summary

router = APIRouter(
    prefix="/summary",
    tags=["Summary"],
)


@router.post("/", response_model=SummaryResponse, summary="Summarize a text using GPT")
async def summarize_text(request: SummaryRequest):
    try:
        summary = await generate_summary(request.text)
        return SummaryResponse(summary=summary)
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Error generating summary: {str(e)}"
        )
