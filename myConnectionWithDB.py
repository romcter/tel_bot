import pymysql.cursors


# Функция возвращает connection.
def getConnection():
    # Вы можете изменить параметры соединения.
    connection = pymysql.connect(host='localhost',
                                user='root',
                                password='1029384756',
                                db='telegram_bot',
                                charset='utf8mb4',
                                cursorclass=pymysql.cursors.DictCursor)
    return connection