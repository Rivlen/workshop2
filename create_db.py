from psycopg2 import connect, OperationalError, sql


def create_db(db_name):
    sql_create_db = f"CREATE DATABASE {db_name};"
    try:
        cnx = connect(
            user="postgres",
            password="coderslab",
            host="localhost",
            port='5433'
        )
        cnx.autocommit = True
        cursor = cnx.cursor()
        cursor.execute(sql_create_db)
        print("Database created")
    except OperationalError as err:
        print(err)
    else:
        cursor.close()
        cnx.close()


def connect_to_db(db_name):
    try:
        cnx = connect(
            user='postgres',
            password='coderslab',
            host='localhost',
            port='5433',
            database=db_name
        )
        cnx.autocommit = True
        cursor = cnx.cursor()
        print('Connected')
        return cnx, cursor
    except OperationalError as err:
        print('Connection error')
        raise ValueError(f'Connection error: {err}')


def query_create_tb_users(db_connector):
    create_table_query = sql.SQL("""
                        CREATE TABLE IF NOT EXISTS users (
                            id SERIAL PRIMARY KEY,
                            username VARCHAR(255),
                            hashed_password VARCHAR(80)
                        );
                    """)
    try:
        with connect(**db_connector) as cnx:
            cnx.autocommit = True
            cursor = cnx.cursor()
            cursor.execute(create_table_query)
    except OperationalError as err:
        print(err)


db = 'workshop2'
connector = {
    'user': 'postgres',
    'password': 'coderslab',
    'host': 'localhost',
    'port': '5433',
    'database': 'db_name'
}
create_db(db)
# query_create_tb_users(connector)
