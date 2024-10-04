import openai
from app.core.config import settings
from app.prompts.summary_prompts import get_summary_prompt
from app.utils.gpt_models import GPTModel

openai.api_key = settings.OPEN_AI_KEY


async def generate_summary(text: str, model: GPTModel = GPTModel.GPT_4) -> str:
    # Llamada a la API de OpenAI con el prompt para generar resúmenes
    response = openai.chat.completions.create(
        model=model.value, messages=get_summary_prompt(text), temperature=0.7
    )

    return response.choices[0].message.content
