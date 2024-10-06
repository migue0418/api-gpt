from fastapi import APIRouter, HTTPException
from app.schemas.summary import GPTBasicTextResponse, GPTBasicTextRequest
from app.external_services.gpt_service import generate_summary
from app.external_services.gpt_service import rewrite_document

router = APIRouter(
    prefix="/gpt",
    tags=["GPT Text Operations"],
)


@router.post(
    "/summary",
    response_model=GPTBasicTextResponse,
    summary="Summarize a text using GPT",
)
async def summarize_text(request: GPTBasicTextRequest):
    try:
        summary = await generate_summary(request.text)
        return GPTBasicTextResponse(summary=summary)
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Error generating summary: {str(e)}"
        )


@router.post(
    "/rewrite-style",
    response_model=GPTBasicTextResponse,
    summary="Summarize a text using GPT",
)
async def rewrite_text(request: GPTBasicTextRequest):
    try:
        summary = await rewrite_document(request.text)
        return GPTBasicTextResponse(summary=summary)
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Error rewriting the text: {str(e)}"
        )
