from langchain_community.agent_toolkits import SQLDatabaseToolkit
from langchain_community.utilities import SQLDatabase
from core.llm_config import llm_model_config

from langchain_core.tools import tool

# define db
db = SQLDatabase.from_uri("sqlite:///Chinook.db")

toolkit = SQLDatabaseToolkit(db=db, llm=llm_model_config())
tools = toolkit.get_tools()

def get_list_tables_tool():
    return next(tool for tool in tools if tool.name == "sql_db_list_tables")

def get_schema_tool():
    return next(tool for tool in tools if tool.name == "sql_db_schema")

# testing the function
# list_tables_tool = get_llist_tables_tool()
# print(list_tables_tool.invoke(""))
# get_schema_tool = get_get_schema_tool()
# print(get_schema_tool.invoke("Artist"))

@tool
def db_query_tool(query: str) -> str:
    """
    Execute a SQL query against the database and get back the result.
    If the query is not correct, an error message will be returned.
    If an error is returned, rewrite the query, check the query, and try again.
    """
    result = db.run_no_throw(query)
    if not result:
        return "Error: Query failed. Please rewrite your query and try again."
    return result


# print(db_query_tool.invoke("SELECT * FROM Artist LIMIT 10;"))