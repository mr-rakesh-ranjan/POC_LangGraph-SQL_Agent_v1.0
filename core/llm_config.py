from langchain_openai import ChatOpenAI
from dotenv import load_dotenv, find_dotenv
import os

load_dotenv(find_dotenv())

def llm_model_config():
    return ChatOpenAI(
        model="gpt-4o",
        api_key=os.getenv("OPENAI_API_KEY"),
        temperature=0,
    )