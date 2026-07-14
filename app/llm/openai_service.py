from openai import OpenAI

from app.core.config import settings


class OpenAIService:
    def __init__(self):
        self.client = OpenAI(
            api_key=settings.openai_api_key
        )

    def generate_answer(self, context: str, question: str):

        prompt = f"""
You are an AI Knowledge Assistant.

Answer ONLY using the supplied context.

If the answer cannot be found in the context,
respond with:

"I couldn't find that information in the uploaded documents."

-------------------------
Context
-------------------------

{context}

-------------------------
Question
-------------------------

{question}
"""

        response = self.client.chat.completions.create(
            model=settings.model_name,
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            temperature=0,
        )

        return response.choices[0].message.content