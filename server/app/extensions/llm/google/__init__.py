from calendar import c
import google.generativeai as genai
from app.config import settings
from openai import OpenAI

client = OpenAI(api_key=settings.GOOGLE_API_KEY, base_url=settings.GOOGLE_BASE_URL)


class GoogleAPI:
    def __init__(self, api_key, base_url):
        self.client = OpenAI(api_key=api_key, base_url=base_url)

    async def chat_completions(self, model_name: str, messages: list, **kwargs):
        response = self.client.chat.completions.create(
            model=model_name,
            messages=messages,
            **kwargs,
        )
        return response.choices[0].message.content

    async def stream_chat_completions(self, model_name: str, messages: list, **kwargs):
        response = self.client.chat.completions.create(
            model=model_name,
            messages=messages,
            stream=True,
            **kwargs,
        )
        for chunk in response:
            if chunk.choices:
                print(chunk.choices[0].delta.content)
                yield "data: " + chunk.choices[0].delta.content + "\n\n"
