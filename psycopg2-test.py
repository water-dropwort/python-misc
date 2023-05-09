import psycopg2
from configparser import ConfigParser


def config(filename="database.ini", section="postgresql"):
    parser = ConfigParser()
    parser.read(filename)

    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]

    return db

db = config()

with psycopg2.connect(
        host=db["host"],
        database=db["database"],
        user=db["user"],
        password=db["password"]
    ) as conn:

    cur = conn.cursor() # a cursor does not support a with statement.

    cur.execute("CREATE TABLE py_test (id SERIAL PRIMARY KEY, weight REAL, height REAL);")

    cur.execute("SELECT * FROM pg_tables WHERE tablename = 'py_test';")
    print("[*] ", cur.fetchone())

    cur.execute("INSERT INTO py_test (weight, height) VALUES (165.8, 54.6);")

    cur.execute("SELECT * FROM py_test;")
    print("[*] ", cur.fetchone())
    
    conn.rollback()

    cur.execute("SELECT * FROM pg_tables WHERE tablename = 'py_test';")
    print("[*] ", cur.fetchone())

    cur.close()

print("[*] end of this script")
