from create_db import *
from models import User, Message

db = 'workshop2'

# creating db
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

