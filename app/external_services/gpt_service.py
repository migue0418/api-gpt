import openai
from app.core.config import settings
from app.prompts.text_prompts import get_summary_prompt
from app.prompts.text_prompts import get_rewrite_prompt
from app.utils.gpt_models import GPTModel

openai.api_key = settings.OPEN_AI_KEY


async def generate_summary(text: str, model: GPTModel = GPTModel.GPT_4) -> str:
    # Llamada a la API de OpenAI con el prompt para generar resúmenes
    response = openai.chat.completions.create(
        model=model.value, messages=get_summary_prompt(text), temperature=0.7
    )

    return response.choices[0].message.content


async def rewrite_document(text: str, model: GPTModel = GPTModel.GPT_4) -> str:
    # Llamada a la API de OpenAI con el prompt para reescribir documentos
    response = openai.chat.completions.create(
        model=model.value,
        messages=get_rewrite_prompt(text=text, style="formal"),
        temperature=0.7,
    )

    return response.choices[0].message.content
