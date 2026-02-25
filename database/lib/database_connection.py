import psycopg
from psycopg.rows import dict_row

def connect_to_db() -> psycopg.Connection:
    seed_path = "seeds/extension_db.sql"
    content = ""
    with open(seed_path, "r") as f:
        content = f.read()
    
    connstr = "postgresql://localhost/extension_db"
    conn = psycopg.connect(connstr, row_factory=dict_row)

    with conn.cursor() as cursor:
        cursor.execute(content)
        conn.commit()

    return conn

