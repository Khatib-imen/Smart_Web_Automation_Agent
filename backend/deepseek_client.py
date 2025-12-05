from openai import OpenAI

client = OpenAI(
    base_url="***",
    api_key="***"
)

def query_deepseek(prompt: str) -> str:
    """Appelle l'API DeepSeek et retourne la réponse complète."""
    completion = client.chat.completions.create(
        model="deepseek-ai/deepseek-v3.1-terminus",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2,
        top_p=0.7,
        max_tokens=8192,
        extra_body={"chat_template_kwargs": {"thinking": True}},
        stream=True
    )

    response_text = ""
    for chunk in completion:
        reasoning = getattr(chunk.choices[0].delta, "reasoning_content", None)
        if reasoning:
            response_text += reasoning
        if chunk.choices[0].delta.content is not None:
            response_text += chunk.choices[0].delta.content
    return response_text


