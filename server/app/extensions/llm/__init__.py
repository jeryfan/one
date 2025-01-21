from fastapi.responses import StreamingResponse
from openai import OpenAI


def stream_response(contentStream):
    return StreamingResponse(contentStream, media_type="text/event-stream")


class ModelChatCompletion:
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
