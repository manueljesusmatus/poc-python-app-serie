from model.serie import Serie
from mysql.connector.connection import MySQLConnection, MySQLCursor
from logger.logger import CustomLogger
class SerieRepository:
    logger: CustomLogger
    db_connection: MySQLConnection
    db_cursor: MySQLCursor

    def __init__(self, db_cursor, db_connection) -> None:
        self.db_cursor = db_cursor
        self.db_connection = db_connection
        self.logger = CustomLogger()
        pass

    def findAll(self) -> list:
        try:
            query = "SELECT * FROM series.serie"
            self.db_cursor.execute(query)
            result = self.db_cursor.fetchall()
            return [Serie(registro) for registro in result]
        except Exception as e: 
            self.logger.logger.error(e)
    
    def findOneById(self, id) -> Serie:
        try:
            query = "SELECT * FROM series.serie s WHERE s.id = %d"
            self.db_cursor.execute(query % int(id))
            result = self.db_cursor.fetchone()
            return result
        except Exception as e: 
            self.logger.logger.error(e)

    def create(self, serie: Serie) -> int:
        try:
            query = "INSERT INTO series.serie (id, tipo, nombre, imagen, url) VALUES (%s, %s, %s, %s, %s)"
            vals = (str(serie.id), serie.tipo, serie.nombre, serie.imagen, serie.url)
            self.db_cursor.execute(query, vals)
            self.db_connection.commit()
            result = self.db_cursor.lastrowid()
            return result
        except Exception as e: 
            self.logger.logger.error(e)