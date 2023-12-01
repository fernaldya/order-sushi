import pymysql
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

class DatabaseHandler:
  def __init__(self, host, user, password, db, port=3306):
    self.host = host
    self.user = user
    self.password = password
    self.db = db
    self.port = port

  def connect(self):
    return pymysql.connect(
      host=self.host,
      user=self.user,
      password=self.password,
      db=self.db,
      port=self.port,
      charset='utf8mb4',
      cursorclass=pymysql.cursors.DictCursor
    )

  def fetch_data(self, query):
    connection = self.connect()
    try:
      with connection.cursor() as cursor:
        logger.info('Executing query: %s', query)
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    finally:
      connection.close()
