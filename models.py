from psycopg2 import connect, OperationalError, sql, errors


class User:
    def __init__(self):
        self._id = -1
        self.username = None
        self._hashed_password = None

    @property
    def id(self):
        return self._id

    @property
    def hashed_password(self):
        return self._hashed_password

    @hashed_password.setter
    def hashed_password(self, password):
        self._hashed_password = password

    def load_user_by_username(self, db_connector):
        table_query = sql.SQL("""
                            SELECT *
                            FROM {table_name}
                            WHERE username = {username}
                        """).format(table_name=sql.Identifier('users'),
                                    username=sql.Literal(self.username)
                                    )
        try:
            with connect(**db_connector) as cnx:
                cnx.autocommit = True
                cursor = cnx.cursor()
                cursor.execute(table_query)
                return cursor.fetchall()
        except OperationalError as err:
            print(err)

    def load_user_by_id(self, db_connector, user_id):
        table_query = sql.SQL("""
                            SELECT *
                            FROM {table_name}
                            WHERE id = {id}
                        """).format(table_name=sql.Identifier('users'),
                                    id=sql.Literal(user_id)
                                    )
        try:
            with connect(**db_connector) as cnx:
                cnx.autocommit = True
                cursor = cnx.cursor()
                cursor.execute(table_query)
                temp_user = cursor.fetchall()[0]
                self._id = temp_user[0]
                self.username = temp_user[1]
                self._hashed_password = temp_user[1]

        except OperationalError as err:
            print(err)
        except IndexError as err:
            print(err)

    def load_all_users(self, db_connector):
        table_query = sql.SQL("""
                            SELECT *
                            FROM {table_name}
                        """).format(table_name=sql.Identifier('users'))
        try:
            with connect(**db_connector) as cnx:
                cnx.autocommit = True
                cursor = cnx.cursor()
                cursor.execute(table_query)
                return cursor.fetchall()
        except OperationalError as err:
            print(err)

    def save_to_db(self, db_connector):
        if self.load_user_by_username(db_connector):
            table_query = sql.SQL("""
                                UPDATE {table_name}
                                SET hashed_password = {password}
                                WHERE username = {username};
                            """).format(table_name=sql.Identifier('users'),
                                        username=sql.Literal(self.username),
                                        password=sql.Literal(self._hashed_password)
                                        )
        else:
            table_query = sql.SQL("""
                                INSERT INTO {table_name} (username, hashed_password)
                                VALUES ({username}, {password});
                            """).format(table_name=sql.Identifier('users'),
                                        username=sql.Literal(self.username),
                                        password=sql.Literal(self._hashed_password)
                                        )
        try:
            with connect(**db_connector) as cnx:
                cnx.autocommit = True
                cursor = cnx.cursor()
                cursor.execute(table_query)
        except OperationalError as err:
            print(err)

    def delete(self, db_connector):
        if self.load_user_by_username(db_connector):
            table_query = sql.SQL("""
                                DELETE FROM {table_name}
                                WHERE username = {username};
                            """).format(table_name=sql.Identifier('users'),
                                        username=sql.Literal(self.username)
                                        )
            try:
                with connect(**db_connector) as cnx:
                    cnx.autocommit = True
                    cursor = cnx.cursor()
                    cursor.execute(table_query)
            except OperationalError as err:
                print(err)
        else:
            print("No such user in the database")


class Message:
    def __init__(self):
        self._id = -1
        self.from_id = None
        self.to_id = None
        self.text = None
        self.creation_data = None

    @property
    def id(self):
        return self._id

    def load_all_messages(self, db_connector):
        table_query = sql.SQL("""
                            SELECT *
                            FROM {table_name}
                        """).format(table_name=sql.Identifier('messages'))
        try:
            with connect(**db_connector) as cnx:
                cnx.autocommit = True
                cursor = cnx.cursor()
                cursor.execute(table_query)
                return cursor.fetchall()
        except OperationalError as err:
            print(err)

    def save_to_db(self, db_connector):
        table_query = sql.SQL("""
                            INSERT INTO {table_name} (from_id, to_id, text)
                            VALUES ({from_id}, {to_id}, {text});
                        """).format(table_name=sql.Identifier('messages'),
                                    from_id=sql.Literal(self.from_id),
                                    to_id=sql.Literal(self.to_id),
                                    text=sql.Literal(self.text)
                                    )
        try:
            with connect(**db_connector) as cnx:
                cnx.autocommit = True
                cursor = cnx.cursor()
                cursor.execute(table_query)
        except OperationalError as err:
            print(err)
