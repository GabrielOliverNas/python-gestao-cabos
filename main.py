import mysql.connector
from mysql.connector import Error

try:

    print('-------------------')
    connection = mysql.connector.connect(
        host='localhost',
        database='projeto-faculdade',
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

        # Insert a record into CABOS
        # sql_insert_query = "INSERT INTO cabos(idCabo, nome, tamanho, cor, dataEntradaCabo, vidaUtil) VALUES ('312312','HDMI', 2.0,'preto', NOW(),'60')"
        # cursor.execute(sql_insert_query)
        # connection.commit()
        # print('Insert na base')

        # Insert a record into FUNCIONARIOS
        # sql_insert_query = "INSERT INTO funcionario(idFuncionario, nome, telefone) VALUES ('xy.98-Ah 77','Josiano Robinsom Mathias','(81)9 1818-1919')"
        # cursor.execute(sql_insert_query)
        # connection.commit()
        # print('Insert na base')

        # Select all a record
        # select_join_table = "SELECT fn.nome, fn.telefone, cb.nome, cb.tamanho FROM statuscabos sc JOIN funcionario fn ON sc.idFuncionario = fn.idFuncionario JOIN cabos cb ON sc.idCabo = cb.idCabo"
        # cursor.execute(select_join_table)
        # records = cursor.fetchall()
        # print('Registros na base: ', records)

except Error as e:
    print('Erro ao conectar..', e)
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")
