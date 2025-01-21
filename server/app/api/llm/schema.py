from pydantic import BaseModel


class ChatCompletion(BaseModel):

    messages: list
    model_name: str = "gemini-1.5-flash"
    stream: bool = True
