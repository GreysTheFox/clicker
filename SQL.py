import pymysql
import config

try:
    connection = pymysql.connect(
        host = config.host,
        port = 3306,
        user = config.user,
        password = config.password,
        database = config.db_name,
        cursorclass = pymysql.cursors.DictCursor
    )
    print('succes')
except Exception as ex:
    print('connection refused')
    print(ex)
