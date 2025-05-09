from langchain_core.prompts import ChatPromptTemplate
from core.llm_config import llm_model_config
from core.toolkit import db_query_tool
# from core.toolkit import db_query_tool
# from sql_schema import db_query_tool

query_pal_schema = """
CREATE DATABASE BusinessRegistrationDB_EN_ES
COLLATE Latin1_General_CI_AS;

USE BusinessRegistrationDB_EN_ES;

-- Create PersonID_PIN Table, stores personal identification details related to individuals involved in business registration.
CREATE TABLE [en_es_chatbot].PersonID_PIN (
    person_id_number NVARCHAR(50) PRIMARY KEY,
    document_type NVARCHAR(100),
    login_PIN NVARCHAR(10)
);

-- Create BusinessRegistration Table, stores detailed information about business registration.
CREATE TABLE [en_es_chatbot].BusinessRegistration (
    registration_number NVARCHAR(100) PRIMARY KEY,
    type_of_person_en NVARCHAR(50),
    type_of_person_es NVARCHAR(50),
    person_id_number NVARCHAR(50),
    full_name NVARCHAR(255),
    birth_date DATE,
    gender_en NVARCHAR(10),
    gender_es NVARCHAR(10),
    phone_number NVARCHAR(20),
    email_id NVARCHAR(255),
    field_of_study_en NVARCHAR(255),
    field_of_study_es NVARCHAR(255),
    check_digit INT,
    business_stage_en NVARCHAR(50),
    business_stage_es NVARCHAR(50),
    start_year INT,
    business_reason_es NVARCHAR(1000),
    business_reason_en NVARCHAR(1000),
    number_of_employees INT,
    location_province_en NVARCHAR(255),
    location_province_es NVARCHAR(255),
    location_district_en NVARCHAR(255),
    location_district_es NVARCHAR(255),
    location_township_en NVARCHAR(255),
    location_township_es NVARCHAR(255),
    cell_number NVARCHAR(20),
    company_activity_general_es NVARCHAR(1000),
    company_activity_general_en NVARCHAR(1000),
    company_activity_specific_es NVARCHAR(1000),
    company_activity_specific_en NVARCHAR(1000),
    nearest_region_en NVARCHAR(100),
    nearest_region_es NVARCHAR(100),
    business_classification_en NVARCHAR(100),
    business_classification_es NVARCHAR(100),
    is_taxable BIT,
    registration_amount_total DECIMAL(10, 0),
    registration_amount_paid DECIMAL(10, 0),
    registration_amount_due DECIMAL(10, 0),
    CONSTRAINT FK_BusinessRegistration_PersonID_PIN FOREIGN KEY (person_id_number) 
        REFERENCES [en_es_chatbot].PersonID_PIN(person_id_number)
);

-- Create BusinessRegistrationDocuments Table, stores information about documents related to business registration.
CREATE TABLE [en_es_chatbot].BusinessRegistrationDocuments (
    registration_number NVARCHAR(100),
    document_type_en NVARCHAR(100),
    document_type_es NVARCHAR(100),
    document_submitted_or_not BIT,  -- True or False
    submitted_date DATETIME,
    document_URL NVARCHAR(255),
    CONSTRAINT FK_UploadedDocuments_Registration FOREIGN KEY (registration_number) 
        REFERENCES [en_es_chatbot].BusinessRegistration(registration_number)
);

-- Create BusinessRegistrationProcessSteps Table, stores information about the various steps involved in the business registration process.
CREATE TABLE [en_es_chatbot].BusinessRegistrationProcessSteps (
    registration_number NVARCHAR(100),
    step_sequence_en NVARCHAR(50),
    step_sequence_es NVARCHAR(50),
    step_datetime DATETIME,
    step_status_en NVARCHAR(50) CHECK (step_status_en IN ('Not Started', 'Started', 'WaitingOnInformation', 'Done')),
    step_status_es NVARCHAR(50) CHECK (step_status_es IN ('Not Started', 'Started', 'WaitingOnInformation', 'Done')),
    step_reviewer_name NVARCHAR(255),  -- Renamed from step_reviewer
    step_reviewer_comment_en NVARCHAR(1000),
    step_reviewer_comment_es NVARCHAR(1000),
    CONSTRAINT FK_ProcessSteps_Registration FOREIGN KEY (registration_number) 
        REFERENCES [en_es_chatbot].BusinessRegistration(registration_number)
);"""

query_check_system = """You are a SQL expert with a strong attention to detail.

Double check the MS-SQL query for common mistakes, including:
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

# query_check_prompt = ChatPromptTemplate.from_messages(
#     [("system", query_check_system), ("placeholder", "{messages}")]
# )
# query_check = query_check_prompt | llm_model_config().bind_tools(
#     [db_query_tool], tool_choice="required"
# )

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
