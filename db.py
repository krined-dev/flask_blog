import mysql.connector
import configparser
from mysql.connector import errorcode

config = configparser.ConfigParser()
config.read('config.ini')
host = config['mysqlDB']['host']
user = config['mysqlDB']['user']
password = config['mysqlDB']['pass']
db = config['mysqlDB']['db']


