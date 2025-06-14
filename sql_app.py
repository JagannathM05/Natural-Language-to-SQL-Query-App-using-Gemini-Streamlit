import streamlit as st
import google.generativeai
import dotenv
import sqlite3
import os
from dotenv import load_dotenv
import google.generativeai as genai


load_dotenv()
genai.configure(api_key=os.getenv("google_api_key"))
model=genai.GenerativeModel('gemini-1.5-flash')


def get_gemini_response(prompt,question):
    response=model.generate_content([prompt,question])
    parts=response.candidates[0].content.parts
    text=''.join(part.text for part in parts)
    return text


def read_sql_query(sql,db):
    connection=sqlite3.connect(db)
    cursor=connection.cursor()
    cursor.execute(sql)
    rows=cursor.fetchall()
    connection.commit()
    connection.close()
    return rows


prompt = """
    You are an expert in converting english questions to SQL query.
    The SQL database has the table name EMPLOYEE and has 
    the following columns -  EMP_NAME, EMP_ID, DESIGNATION, EMP_AGE 
    \n\n
    -----------------------------------------------------
    Examples:
    \nExample 1 - How many entries of records are present?, 
    the SQL command will be something like this 
    SELECT COUNT(*) FROM EMPLOYEE ;
    
    \nExample 2 - Tell me all the employees with designation Data Engineer?, 
    the SQL command will be something like this SELECT * FROM EMPLOYEE 
    where DESIGNATION='Data Engineer'; 
    ------------------------------------------------------

    also the sql code should not have  in beginning or end.

    If generate SQL query contains triple quotes  ( or ''') in beginning 
    and end then strictly remove the triple quotes and provide me only the 
    SQL query. 
    """

st.set_page_config(page_title="asksql")
st.header("application to retrive sql data using english")
question=st.text_input("enter your question",key="input")
submit=st.button("Submit")

if submit:
    response=get_gemini_response(prompt,question)
    print(response)
    response=read_sql_query(response,"employee.db")
    st.subheader("the llm response is")
    for row in response:
        st.write(row)