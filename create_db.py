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

query_create_table_users = sql.SQL("""
    CREATE TABLE IF NOT EXISTS {table_name} (
        id SERIAL,
        name VARCHAR(50) NOT NULL,
        email VARCHAR(120) UNIQUE,
        password VARCHAR(60) DEFAULT 'ala',
        PRIMARY KEY (id)
    )
""").format(table_name=sql.Identifier('users'))

with cnx:
    try:
        cursor.execute(query_create_table_users)
    except DatabaseError as err:
        print(err)

query_create_table_message = sql.SQL("""
    CREATE TABLE {table_name} (
        id SERIAL,
        from_id VARCHAR(255) NOT NULL
    )
""").format(table_name=sql.Identifier('test1234'))

# with cnx:
#     try:
#         cursor.execute(query_create_table_message)
#     except DatabaseError as err:
#         print(err)

query_select = sql.SQL("""
    SELECT *
    FROM user
""").format(table_name=sql.Identifier('user'))

query_insert = sql.SQL("""
    INSERT INTO user (username, hashed_password)
    VALUES ('Jarosław', 'Kowalski');
""").format(table_name=sql.Identifier('user'))

# with cnx:
#     try:
#         cursor.execute(query_select)
#         print(cursor.fetchall())
#     except DatabaseError as err:
#         print(err)

query_drop_user = sql.SQL("""
    DROP TABLE user
""").format(table_name=sql.Identifier('user'))

# with cnx:
#     try:
#         cursor.execute(query_drop_user)
#     except DatabaseError as err:
#         print(err)
