import mysql.connector
from mysql.connector import Error

try:

    print('-------------------')
    connection = mysql.connector.connect(
        host='localhost',
        database='teste01',
        user='root',
        password='')

    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL database... MySQL Server version on ", db_Info)

        cursor = connection.cursor()

        # Delete a record
        # sql_Delete_query = 'Delete from Laptop where id = 2'
        # cursor.execute(sql_Delete_query)
        # connection.commit()
        # print('number of rows deleted', cursor.rowcount)

        # Insert a record
        # sql_insert_query = "insert into laptop (id, name, price) VALUES (1, 'Marcos', 2.0)"
        # cursor.execute(sql_insert_query)
        # connection.commit()
        # print('Insert na base')

        # Select byId a record
        # sql_select_Query = "select * from Laptop where name = 'Lenovo ThinkPad P71'"
        # cursor.execute(sql_select_Query)
        # records = cursor.fetchall()
        # print('records: ', records)

        # Select all a record
        # cursor.execute('select * from Laptop')
        # records = cursor.fetchall()
        # print('Registros na base: ', records)

except Error as e:
    print('Erro ao conectar..', e)
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")
