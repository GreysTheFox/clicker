import pymysql
import config
from Settings import Settings

def initialize():
    try:
        connection = pymysql.connect(
            host = config.host,
            port = 3306,
            user = config.user,
            password = config.password,
            database = config.db_name,
            cursorclass = pymysql.cursors.DictCursor
        )
        return connection

    except Exception as ex:
        print('connection refused')
        print(ex)
        return None

def new_member(name, password):
    connection = initialize()
    with connection.cursor() as cursor:
        insert_query = f'INSERT INTO `players` (`name`, `password`) VALUES ("{name}", "{password}")'
        cursor.execute(insert_query)
        connection.commit()
        Settings.name = name
        Settings.password = password 
        Settings.scrore = 0

def check_member(name, password):
    connection = initialize()
    with connection.cursor() as cursor:
        select_all_data =  f'SELECT score FROM `players` WHERE `name` = "{name}" AND `password` = "{password}";'
        cursor.execute(select_all_data)
        row = cursor.fetchall()
        if len(row) > 0:
            print(type(Settings.score))
            Settings.name = name
            Settings.password = password 
            Settings.score = row[0]['score'] 
            return True
        else:
            return False

def send_score(name, password, score):
    connection = initialize()
    with connection.cursor() as cursor:
        send = f'UPDATE `players` SET `score` = "{score}" WHERE `players`.`name` = "{name}" AND `players`.`password` = "{password}";'
        cursor.execute(send)
        connection.commit()