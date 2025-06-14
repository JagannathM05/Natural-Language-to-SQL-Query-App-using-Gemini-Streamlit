import sqlite3
 
connection = sqlite3.connect("employee.db")

cursor = connection.cursor()

table_info = """
CREATE TABLE EMPLOYEE(EMP_NAME VARCHAR(25), EMP_ID VARCHAR(25), DESIGNATION VARCHAR(25), EMP_AGE INT);
"""

try:
    cursor.execute(table_info)
except:
    pass

cursor.execute(''' Insert Into EMPLOYEE values('Shashank','XY101','TESTER',23)''')
cursor.execute(''' Insert Into EMPLOYEE values('Arun','XY102','DEVELOPER',43)''')
cursor.execute(''' Insert Into EMPLOYEE values('Sarvesh','XY103','NLP ENGINEER',23)''')
cursor.execute(''' Insert Into EMPLOYEE values('Lakshya','XY104','AI DEVELOPER',32)''')
cursor.execute(''' Insert Into EMPLOYEE values('Sanjya','XY105','DATA ANALYST',23)''')

print("The inserted Records are:")
data = cursor.execute('''Select * from  EMPLOYEE''')

for row in data:
    print(row)

connection.commit()
connection.close()