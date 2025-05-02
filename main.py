
# ----------------main.py------------------
from core.workflow import app
print(app.get_graph())

while True:
    user_query = input("Enter your query: ")
    if user_query.lower() == "exit":
        break
    messages = app.invoke({"messages": [("user", user_query)]})
    json_str = messages["messages"][-1].tool_calls[0]["args"]["final_answer"]
    print(json_str)
    
    
# messages = app.invoke({"messages": [("user", "Which artist main genre is Rock?")]})
# messages = app.invoke({"messages": [("user", "How many employees get hired in year 2002? and give the names.")]})
# messages = app.invoke({"messages": [("user", "give me  details of all employees in db")]})
# messages = app.invoke({"messages": [("user", "what are the basic documents required for business registration?")]})  # type: ignore
# messages = app.invoke(
#     # {"messages": [("user", "Which artist main genre is Rock?")]}  # type: ignore
#     # {"messages": [("user", "How many employees get hired in year 2002? and give the names.")]}  # type: ignore
#     # {"messages": [("user", "give me  details of all employees in db")]}  # type: ignore
#     # {"messages": [("user", "what are the basic documents required for business registration?")]}  # type: ignore
#     {"messages": [("user", "what are the basic documents required for business registration?")]}  # type: ignore
    
# )
# json_str = messages["messages"][-1].tool_calls[0]["args"]["final_answer"]
# # json_str = messages["messages"]
# print(json_str)