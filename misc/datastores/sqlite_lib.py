from sqlite3 import connect, version, Error


def create_db(db_file_path):
    "create database"
    conn = connect(db_file_path)
    print(version)
    return conn.close()


def connection(db_file_path):
    "create database connection"
    return connect(db_file_path)


def query(conn, sql, variable_bindings=None):
    "run a test query"
    cur = conn.cursor()
    status = cur.execute(sql, variable_bindings) if variable_bindings else cur.execute(sql)
    print(f"query status: {status}")
    return cur.fetchall()

