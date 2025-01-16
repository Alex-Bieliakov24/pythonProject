import pymysql

dbconfig = {
    'host': 'ich-edit.edu.itcareerhub.de',
    'user': 'ich1',
    'password': 'ich1_password_ilovedbs',
    'database': '050824_Bieliakov_sakila',
}

try:
    connection = pymysql.connect(**dbconfig)
    print("Connection successful!")
    connection.close()
except pymysql.MySQLError as e:
    print(f"Database error: {e}")
