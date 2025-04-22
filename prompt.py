from langchain_core.prompts import ChatPromptTemplate
from core.llm_config import llm_model_config
from core.toolkit import db_query_tool

query_check_system = """You are a SQL expert with a strong attention to detail.
Double check the SQLite query for common mistakes, including:
- Using NOT IN with NULL values
- Using UNION when UNION ALL should have been used
- Using BETWEEN for exclusive ranges
- Data type mismatch in predicates
- Properly quoting identifiers
- Using the correct number of arguments for functions
- Casting to the correct data type
- Using the proper columns for joins

If there are any of the above mistakes, rewrite the query. If there are no mistakes, just reproduce the original query.

You will call the appropriate tool to execute the query after running this check."""

query_check_prompt = ChatPromptTemplate.from_messages(
    [("system", query_check_system), ("placeholder", "{messages}")]
)
query_check = query_check_prompt | llm_model_config().bind_tools(
    [db_query_tool], tool_choice="required"
)

# res = query_check.invoke({"messages": [("user", "SELECT * FROM Artist LIMIT 10;")]})
# print(res)

def query_check_prompt_func(messages):
    """
        Function to check the SQL query for common mistakes.
        If there are any mistakes, rewrite the query.
        If there are no mistakes, just reproduce the original query.
    """
    query_check_prompt = ChatPromptTemplate.from_messages(
        [("system", query_check_system), ("placeholder", "{messages}")]
    )
    query_check = query_check_prompt | llm_model_config().bind_tools(
        [db_query_tool], tool_choice="required"
    )
    return query_check.invoke({"messages": messages})