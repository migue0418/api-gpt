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


def get_rewrite_prompt(text: str, style: str = "formal") -> list[str]:
    """
    Prompt para reescribir un documento dado un estilo
    """
    return [
        {
            "role": "system",
            "content": f"""Eres un asistente que reescribe textos.
            Tienes que escribir usando un estilo {style}.""",
        },
        {"role": "user", "content": f"Reescribe el siguiente texto:\n {text}"},
    ]
