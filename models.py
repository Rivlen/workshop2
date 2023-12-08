from psycopg2 import connect, OperationalError, sql, errors


class User:
    def __init__(self):
        self._id = -1
        self.username = None
        self._hashed_password = None

    @property
    def id(self):
        return self._id

    # @id.setter
    # def id(self, number):
    #     self._id = number

    @property
    def hashed_password(self):
        return self._hashed_password

    @hashed_password.setter
    def hashed_password(self, password):
        self._hashed_password = password

    def save_to_db(self, db_connector):
        insert_table_query = sql.SQL("""
                            INSERT INTO {table_name} (username, hashed_password)
                            VALUES  ({username}, {password});
                        """).format(table_name=sql.Identifier('users'),
                                    username=sql.Identifier(self.username),
                                    password=sql.Identifier(self._hashed_password)
                                    )
        try:
            with connect(**db_connector) as cnx:
                cnx.autocommit = True
                cursor = cnx.cursor()
                cursor.execute(insert_table_query)
        except OperationalError as err:
            print(err)
