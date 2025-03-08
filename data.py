#%% CREATE DATABASE
from mysql import connector
import pandas as pd
from dotenv import load_dotenv
import os

load_dotenv()
password = os.getenv("SECRETE_KEY")

# mydb = connector.connect(
#     host='localhost',
#     user='root',
#     password=password
#     )

# mycursor = mydb.cursor()

# mycursor.execute("CREATE DATABASE FinProject")
# mycursor.close()
# mydb.close()

#%% CONNECT & LOAD DATA
# Connect
mydb = connector.connect(
    host='localhost',
    user='root',
    password=password,
    database='FinProject'
    )

query = "SELECT * FROM uci_credit_card;"
df = pd.read_sql(query, con=mydb)
df.head()
df.shape
