from psycopg2 import connect, OperationalError, Error, sql, DatabaseError
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

try:
    # Connect to PostgreSQL DBMS
    con = connect(user='postgres', password='coderslab', host='localhost', port='5433')
    con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cursor = con.cursor()
    # Create database
    create_database_query = f'CREATE DATABASE workshop2'
    cursor.execute(create_database_query)
    print(f"Database 'workshop2' created successfully")

    # Closing the connection
    cursor.close()
    con.close()

except Error as e:
    print(f"An error occurred: {e}")

try:
    cnx = connect(
        user='postgres',
        password='coderslab',
        host='localhost',
        port='5433',
        database='workshop2'
    )

    cursor = cnx.cursor()
    print('Connected')
except OperationalError as err:
    print('Connection error')
    raise ValueError(f'Connection error: {err}')

query_create_table_user = sql.SQL("""
    CREATE TABLE {table_name} (
        id SERIAL,
        username VARCHAR(255) NOT NULL,
        hashed_password VARCHAR(80),
        password VARCHAR(60) DEFAULT 'ala',
        PRIMARY KEY (id)
    )
""").format(table_name=sql.Identifier('user'))

with cnx:
    try:
        cursor.execute(query_create_table_user)
    except DatabaseError as err:
        print(err)
