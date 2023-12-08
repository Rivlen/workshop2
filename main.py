from create_db import *
from models import User


db = 'workshop2'

# connector = {
#     'user': 'postgres',
#     'password': 'coderslab',
#     'host': 'localhost',
#     'port': '5433'
# }
# create_db(connector, db)
# connector['database'] = db

connector = {
    'user': 'postgres',
    'password': 'coderslab',
    'host': 'localhost',
    'port': '5433',
    'database': db
}

# query_create_tb_users(connector)
# query_insert_into_tb(connector)
query_select_tb(connector)
