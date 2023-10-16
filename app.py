import streamlit as st
from langchain.llms import OpenAI
import psycopg2
import os
import urllib.parse as up
from dotenv import load_dotenv

load_dotenv()

up.uses_netloc.append("postgres")
# url = up.urlparse(os.environ["DATABASE_URL"])

# st.write("DB username:", st.secrets["db_username"])
url = up.urlparse(st.secrets["DATABASE_URL"])
conn = psycopg2.connect(database=url.path[1:],
user=url.username,
password=url.password,
host=url.hostname,
port=url.port
)

cursor = conn.cursor()
cursor.execute("SELECT * FROM conversations LIMIT 5")  # Replace with your table name
records = cursor.fetchall()

# Print the retrieved data
for record in records:
    st.write(record)

    st.write("HELLO WORLD")