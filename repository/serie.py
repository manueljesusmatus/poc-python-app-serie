from model.serie import Serie
from mysql.connector.connection import MySQLConnection, MySQLCursor

class SerieRepository:
    db_connection: MySQLConnection
    db_cursor: MySQLCursor

    def __init__(self, db_cursor, db_connection) -> None:
        self.db_cursor = db_cursor
        self.db_connection = db_connection
        pass

    def findAll(self) -> list:
        query = "SELECT * FROM series.serie"
        self.db_cursor.execute(query)
        result = self.db_cursor.fetchall()
        return [Serie(registro) for registro in result]
    
    def findOneById(self, id) -> Serie:
        query = "SELECT * FROM series.serie s WHERE s.id = %s"
        self.db_cursor.execute(query, (id))
        result = self.db_cursor.fetchone()
        return result

    def create(self, serie: Serie) -> int:
        query = "INSERT INTO series.serie (tipo, nombre, imagen, url) VALUES (%s, %s, %s, %s)"
        self.db_cursor.execute(query, (serie.tipo, serie.nombre, serie.imagen, serie.url))
        self.db_connection.commit()
        result = self.db_cursor.lastrowid()
        return result