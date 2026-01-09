from langchain_openai import ChatOpenAI
from packages.common.settings import settings

def get_llm():
    return ChatOpenAI(
        api_key=settings.openai_api_key,
        model=settings.openai_model,
        temperature=0.2,
    )
