from langchain_community.agent_toolkits import SQLDatabaseToolkit
from langchain_community.utilities import SQLDatabase
from langsmith import traceable
from core.llm_config import llm_model_config
# from sql_agent import get_db

from langchain_core.tools import tool

# define db
# db = SQLDatabase.from_uri("sqlite:///Chinook.db")
db = SQLDatabase.from_uri("mssql+pyodbc://spanish_login:Query$1234@sqlserver-spanishchatbot-dev.database.windows.net:1433/CompanyTestDB?driver=ODBC+Driver+18+for+SQL+Server")
# db = SQLDatabase.from_uri("mssql+pyodbc://spanish_login:Query$1234@sqlserver-spanishchatbot-dev.database.windows.net:1433/BusinessRegistrationDB_EN_ES?driver=ODBC+Driver+18+for+SQL+Server")
# db = get_db()

toolkit = SQLDatabaseToolkit(db=db, llm=llm_model_config())
tools = toolkit.get_tools()

# print("tools : ", tools)

@traceable(run_type="tool", name="get list_tables_tool")
def get_list_tables_tool():
    return next(tool for tool in tools if tool.name == "sql_db_list_tables")

@traceable(run_type="tool", name="get schema_tool")
def get_schema_tool():
    return next(tool for tool in tools if tool.name == "sql_db_schema")

# testing the function
# list_tables_tool = get_llist_tables_tool()
# print(list_tables_tool.invoke(""))
# get_schema_tool = get_get_schema_tool()
# print(get_schema_tool.invoke("Artist"))

@tool
@traceable(run_type="tool", name="db_query_tool")
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