from fastapi import APIRouter
from fastapi.responses import JSONResponse, StreamingResponse
from app.config import settings
from app.api.llm.schema import ChatCompletion
from app.extensions.llm.google import GoogleAPI
from app.extensions.llm import stream_response

router = APIRouter(prefix="/llm")


@router.post("/chat/completions")
async def chat_completions(payload: ChatCompletion):
    print("google_chat_completions", payload.model_dump())
    # resp = google_chat_completions(**payload.model_dump())

    google = GoogleAPI(
        api_key=settings.google_api_key, base_url=settings.google_base_url
    )
    if payload.stream:
        return stream_response(
            google.chat_completions(
                model_name=payload.model_name, messages=payload.messages
            )
        )
    else:
        result = await google.chat_completions(
            model_name=payload.model_name, messages=payload.messages
        )
        print(result)
        return JSONResponse({"result": result})
