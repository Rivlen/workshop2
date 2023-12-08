from psycopg2 import connect, OperationalError, sql, errors


def create_db(db_connector, db_name):
    sql_create_db = f"CREATE DATABASE {db_name};"
    try:
        cnx = connect(**db_connector)
        cnx.autocommit = True
        cursor = cnx.cursor()
        cursor.execute(sql_create_db)
        print("Database created")
    except OperationalError as err:
        print(err)
    except errors.DuplicateDatabase as err:
        print(err)
    else:
        cursor.close()
        cnx.close()


def connect_to_db(db_connector):
    try:
        cnx = connect(**db_connector)
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


def query_create_tb_messages(db_connector):
    create_table_query = sql.SQL("""
                        CREATE TABLE IF NOT EXISTS {table_name} (
                        id SERIAL PRIMARY KEY,
                        from_id INTEGER REFERENCES users(id),
                        to_id INTEGER REFERENCES users(id),
                        creation_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                        text VARCHAR(255)
                        );
                    """).format(table_name=sql.Identifier('messages'))
    try:
        with connect(**db_connector) as cnx:
            cnx.autocommit = True
            cursor = cnx.cursor()
            cursor.execute(create_table_query)
    except OperationalError as err:
        print(err)


def query_insert_into_tb(db_connector):
    insert_table_query = sql.SQL("""
                        INSERT INTO {table_name} (username, hashed_password)
                        VALUES  ('random_name123', 'ghu7234r9i8ghbsd12'),
                                ('random_name12343', 'ghu7234r124dfafsdbsd12');
                    """).format(table_name=sql.Identifier('users'))
    try:
        with connect(**db_connector) as cnx:
            cnx.autocommit = True
            cursor = cnx.cursor()
            cursor.execute(insert_table_query)
    except OperationalError as err:
        print(err)


def query_select_tb(db_connector):
    insert_table_query = sql.SQL("""
                        SELECT *
                        FROM {table_name};
                    """).format(table_name=sql.Identifier('users'))
    try:
        with connect(**db_connector) as cnx:
            cnx.autocommit = True
            cursor = cnx.cursor()
            cursor.execute(insert_table_query)
            for row in cursor.fetchall():
                print(row)
    except OperationalError as err:
        print(err)


db = 'workshop2'
connector = {
    'user': 'postgres',
    'password': 'coderslab',
    'host': 'localhost',
    'port': '5433'
}

# create_db(connector, db)

connector['database'] = db

# query_create_tb_users(connector)

# query_insert_into_tb(connector)

query_select_tb(connector)
