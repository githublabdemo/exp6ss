import mysql.connector

db_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="qwe123",
    database="db"
)

cursor = db_connection.cursor()

create_table_query = """
CREATE TABLE IF NOT EXISTS Student (
    sno INT AUTO_INCREMENT PRIMARY KEY,
    sname VARCHAR(255),
    result VARCHAR(50)
)
"""

cursor.execute(create_table_query)

insert_records_query = """
INSERT INTO Student (sname, result) VALUES (%s, %s)
"""

student_data = [
    ("John Doe", "Pass"),
    ("Jane Smith", "Fail"),
    ("Bob Johnson", "Pass")
]

cursor.executemany(insert_records_query, student_data)

db_connection.commit()

select_query = "SELECT * FROM Student"
cursor.execute(select_query)

print("Student Table:")
print("--------------")
for record in cursor.fetchall():
    print(f"Student ID: {record[0]}, Name: {record[1]}, Result: {record[2]}")


cursor.close()
db_connection.close()
