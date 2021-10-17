import sqlite3
# To open a connection with the database.
conn = sqlite3.connect('employees.db')

# To create a cursor object to perform operations on database.
cur = conn.cursor()

# code goes here
# Using the cursor to create the database if the database does not exists
cur.execute("""
CREATE TABLE IF NOT EXISTS employees (
    id INTEGER PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    years_with_company INTEGER DEFAULT 0 
)
""")

cur.executemany("""
INSERT INTO employees (first_name, last_name, email, years_with_company) VALUES (?, ?, ?, ?)
""", [
    ('Kevin', 'Bacon', 'kbacon@example.com', 2),
    ('Josh', 'Brolin', 'jbrolin@example.com', 1),
    ('Kim', 'Dickens', 'kdickens@example.com', 0),
])

# Make sure to commit the connection when you have done some transaction like INSERT.

conn.commit()

for row in cur.execute("SELECT * FROM employees WHERE years_with_company >= 1"):
    print(row[1], "has worked for", row[4], "years")

# closing the cursor object
cur.close()

# closing the connection
conn.close()