import sqlite3


def insert(data):
    # Create connection to transactions database
    conn = sqlite3.connect('transactions.db')

    # Create table records
    cur = conn.cursor()
    cur.execute("DROP TABLE records")
    cur.execute("""CREATE TABLE IF NOT EXISTS records(
                id INT,
                date TEXT,
                amount REAL)""")

    conn.commit()

    # Insert records
    conn.executemany("INSERT INTO records VALUES (?,?,?)", data)
    conn.commit()

    # Close cursor and connection
    cur.close()
    conn.close()
