import mysql.connector
import configparser
from mysql.connector import errorcode

config = configparser.ConfigParser()
config.read('config.ini')
host = config['mysqlDB']['host']
user = config['mysqlDB']['user']
password = config['mysqlDB']['pass']
db = config['mysqlDB']['db']


class OppslagReg:

    def __init__(self) -> None:
        dbconfig = {'host': host,
                    'user': user,
                    'password': password,
                    'database': db, }
        self.configuration = dbconfig

    def __enter__(self) -> 'cursor':
        self.conn = mysql.connector.connect(**self.configuration)
        self.cursor = self.conn.cursor(prepared=True)
        return self

    def __exit__(self, exc_type, exc_val, exc_trace) -> None:
        self.conn.commit()
        self.cursor.close()
        self.conn.close()

    def query(self, sql):
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        return result


