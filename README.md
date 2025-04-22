# POC_LangGraph-SQL_Agent_v1.0

## 📑 Overview

This project is a **Proof of Concept (POC)** demonstrating the integration of **LangGraph** with a SQL database agent. It enables users to query an SQLite database using natural language, dynamically converting the query into SQL using a custom agent workflow.

---

## 📂 Project Structure

  ├── Chinook.db # SQLite sample database 
  ├── Chinook_schema.txt # Schema definition of the database 
  ├── agent.py # Defines agent configuration 
  ├── chinhook.py # Database utility functions 
  ├── core/ # Supporting modules (if any) 
  ├── main.py # Main application entry point 
  ├── prompt.py # Prompt templates for the agent 
  ├── sql_agent.py # SQL agent logic implementation 
  └── utils.py # Helper utilities


---

## 🚀 Features

- **LangGraph Integration** — Uses LangGraph to manage agent execution and workflows.
- **SQL Database Agent** — Converts natural language queries into executable SQL.
- **SQLite Database** — Comes with a sample `Chinook.db` database for demonstration.
- **Prompt Engineering** — Custom prompt templates for accurate query generation.

---

## 🛠️ Technologies Used

- Python 3.x
- LangGraph
- SQLite
- OpenAI API (or other LLM providers)

---

## 📝 Getting Started

### 📥 Clone the Repository

```bash
git clone https://github.com/mr-rakesh-ranjan/POC_LangGraph-SQL_Agent_v1.0.git
cd POC_LangGraph-SQL_Agent_v1.0
```

## 📌 Usage Example

Once running, input your natural language query like:

> _"Show me all tracks by 'AC/DC'"_

The agent will parse the request, generate the appropriate SQL, query the `Chinook.db`, and return the results.

## 📚 Database

-   **Chinook.db**: A pre-built SQLite database representing a digital media store, including tables for artists, albums, tracks, invoices, customers, etc.
    
-   **Chinook_schema.txt**: Schema description for easy reference.
    

## 📈 Future Enhancements

-   Multi-database support (PostgreSQL, MySQL)
    
-   Web interface integration
    
-   Enhanced error handling and query validation
    
-   Support for conversational memory in LangGraph
