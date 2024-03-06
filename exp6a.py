import sqlite3

conn = sqlite3.connect('students.db')

cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS Student (
                    sno INTEGER PRIMARY KEY,
                    sname TEXT,
                    result TEXT)''')

students = [
    ('John', 'Pass'),
    ('Ace', 'Fail'),
    ('Bob', 'Pass')
]
cursor.executemany('INSERT INTO Student (sname, result) VALUES (?, ?)', students)

conn.commit()

cursor.execute('SELECT * FROM Student')
print("Student records:")
for record in cursor.fetchall():
    print(record)

cursor.close()
conn.close()
