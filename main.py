# from core.toolkit import get_list_tables_tool, get_get_schema_tool, db_query_tool

# print(db_query_tool.invoke("SELECT * FROM Artist LIMIT 10;"))

from core.workflow import app

# ------------Testing remain due to Insufficient Quota------------------

# from IPython.display import Image, display
# from langchain_core.runnables.graph import MermaidDrawMethod

# res = display(
#     Image(
#         app.get_graph().draw_mermaid_png(
#             draw_method=MermaidDrawMethod.API,
#         )
#     )
# )

# print(res)

# ----------------main.py------------------
from core.workflow import app
# print(app.get_graph())

messages = app.invoke(
    # {"messages": [("user", "Which artist main genre is Rock?")]}  # type: ignore
    # {"messages": [("user", "How many employees get hired in year 2002? and give the names.")]}  # type: ignore
    # {"messages": [("user", "give me  details of all employees in db")]}  # type: ignore
    {"messages": [("user", "who is the manager of Jane Peacock?")]}  # type: ignore
    
)
json_str = messages["messages"][-1].tool_calls[0]["args"]["final_answer"]
# json_str = messages["messages"]
print(json_str)