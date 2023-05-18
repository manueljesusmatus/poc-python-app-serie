from envparse import env

db_host = env("DB_HOST")
db_port = env.int("DB_PORT")
db_user = env("DB_USER")
db_pass = env("DB_PASS")
db_name = env("DB_NAME")