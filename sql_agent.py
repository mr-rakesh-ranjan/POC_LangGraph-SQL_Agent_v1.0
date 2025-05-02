from langchain_community.utilities import SQLDatabase
from core.llm_config import db_str_config


def get_db():
    # return SQLDatabase.from_uri("sqlite:///Chinook.db")
    return SQLDatabase.from_uri(db_str_config())

# db = get_db()
# print("db : ", db.get_context())
# print("dilect :-> ",db.dialect)
# print("usable tables : ",db.get_usable_table_names())
# print("info tables : ",db.get_table_info())

# res = db.run("SELECT * FROM sqlite_master WHERE type = 'table'; ")
# res = db.run("SELECT * FROM INFORMATION_SCHEMA.TABLES where TABLE_TYPE = 'BASE TABLE';")   
# print(res)
# with open("QueryPal_db.txt", "wb") as file:
#     # Write the content of the response (the file) to the local file
#     file.write(str(res).encode())
#     print(type(res))
# print("File downloaded and saved as Chinook_schema.txt")