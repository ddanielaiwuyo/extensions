import psycopg
from psycopg.rows import dict_row

def connect() -> psycopg.Connection:
    connstr = "postgresql://localhost/extension_db"
    conn = psycopg.connect(connstr, row_factory=dict_row)
    return conn

def seed(conn, seed_path=None):
    if seed_path is None:
        print("  Using default seed path: seeds/extension_db.sql",)
        seed_path = "seeds/extension_db.sql"

    content = ""
    with open(seed_path, "r") as f:
        content = f.read()

    with conn.cursor() as cursor:
        cursor.execute(content)
        conn.commit()
