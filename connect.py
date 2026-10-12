import mysql.connector
from setup import db_host, db_port, db_name, db_user, db_pass

db_connection = mysql.connector.connect(
    host=db_host,
    database=db_name,
    user=db_user,
    passwd=db_pass,
    port=db_port
)