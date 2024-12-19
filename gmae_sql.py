import sqlite3

# Connect to the database (or create it if it doesn't exist)
conn = sqlite3.connect('example.db')
cursor = conn.cursor()

# Create a table
cursor.execute('''
CREATE TABLE IF NOT EXISTS data (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    content TEXT
)
''')

# Read data from the input file
with open('input.txt', 'r') as file:
    lines = file.readlines()

# Insert data into the table
for line in lines:
    cursor.execute('INSERT INTO data (content) VALUES (?)', (line.strip(),))

# Commit the transaction
conn.commit()

# Close the connection
conn.close()
