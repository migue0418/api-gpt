def get_summary_prompt(text: str) -> list[str]:
    """
    Prompt para solicitar un resumen a GPT.
    """
    return [
        {
            "role": "system",
            "content": "Eres un asistente que genera resúmenes. Debes ser claro y conciso.",
        },
        {"role": "user", "content": f"Resume el siguiente texto por favor:\n {text}"},
    ]
