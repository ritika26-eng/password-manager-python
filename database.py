import sqlite3

DB = "passwords.db"


def connect():
    return sqlite3.connect(DB)


def init_db():
    conn = connect()
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS passwords (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            website TEXT,
            username TEXT,
            password TEXT
        )
    """)

    conn.commit()
    conn.close()


def add_password(site, user, password):
    conn = connect()
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO passwords (website, username, password) VALUES (?, ?, ?)",
        (site, user, password)
    )

    conn.commit()
    conn.close()