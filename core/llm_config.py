from langchain_openai import ChatOpenAI
import openai
from langsmith.wrappers import wrap_openai
from dotenv import load_dotenv, find_dotenv
import os

load_dotenv(find_dotenv())

def llm_model_config():
    return ChatOpenAI(
        model="gpt-4o",
        api_key=os.getenv("OPENAI_API_KEY"),
        temperature=0,
    )
    
# def llm_model_config():
#     return wrap_openai(
#         openai.Client()
#     )

def setup_smith_variables():
    os.environ['LANGSMITH_TRACING'] = "true"
    os.environ['LANGSMITH_API_KEY'] = os.getenv("LANGSMITH_API_KEY")
    os.environ['OPENAI_API_KEY'] = os.getenv("OPENAI_API_KEY")

def db_str_config():
    return os.getenv("SQL_DB_URI")