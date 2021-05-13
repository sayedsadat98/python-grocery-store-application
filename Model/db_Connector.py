import datetime
import mysql.connector


class dataBase:


__cnx = None


def get_sql_connection():
    print("Opening mysql connection")
    global __cnx

    if __cnx is None:
        __cnx = mysql.connector.connect(user='root', password='', host='127.0.0.1', database='grocerystore')

    return __cnx
