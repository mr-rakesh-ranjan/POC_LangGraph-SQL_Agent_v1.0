from langchain_community.utilities import SQLDatabase

def get_db():
    return SQLDatabase.from_uri("sqlite:///Chinook.db")

db = get_db()
print(db.dialect)
print(db.get_usable_table_names())
res = db.run("SELECT * FROM sqlite_master WHERE type = 'table'; ")
print(res)
with open("Chinook_schema.txt", "wb") as file:
    # Write the content of the response (the file) to the local file
    file.write(str(res).encode())
    print(type(res))
print("File downloaded and saved as Chinook_schema.txt")