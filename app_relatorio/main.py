'''
    Filename: main.py
    Author: izahterencio@gmail.com
    Date: 2023/09/04
'''


import fdb
from datetime import datetime


'''Função responsável por realizar a conexão com o banco de dados do sistema'''
def connect_database(srvr, pth_db, usr, passwd):
    con = fdb.connect(
        host=srvr,
        database=pth_db,
        user=usr,
        password=passwd)

    return(con)



'''Função responsável por gerar o relatório solicitado pelo usuário'''
def generate_report(start, end):
    file_buff = []

    query = ("SELECT GRUPO.descricao AS GRUPO, "
             "SUM((ITEM.vlr_total + ITEM.vlr_despesa - ITEM.vlr_desc)) AS VAL_VENDIDO "
             "FROM tb_est_grupo AS GRUPO, tb_estoque AS ESTOQUE, tb_nfv_item AS ITEM, "
             "tb_est_identificador AS ESTOQUE_ID, tb_nfvenda AS VENDA "
             "WHERE GRUPO.id_grupo IS NOT NULL AND GRUPO.id_grupo = ESTOQUE.id_grupo AND ESTOQUE.id_estoque = "
             "ESTOQUE_ID.id_estoque AND ESTOQUE_ID.id_identificador = ITEM.id_identificador AND ITEM.id_nfvenda = "
             "VENDA.id_nfvenda AND VENDA.dt_emissao BETWEEN ? AND ? GROUP BY GRUPO.descricao")

    srv_file = open('host_connection_data.txt', 'r')

    # Tratamento dos parâmetros de conexão do servidor
    for f in srv_file:
        f = f[3:len(f)-1]
        file_buff.append(f)

    srv_file.close()

# Para fins de teste, esta funcionalidade de conexão será omitida por enquanto.
'''
    connection = connect_database(file_buff[0],
                                  file_buff[1],
                                  file_buff[2],
                                  file_buff[3])

    cursor = connection.cursor()
    cursor.execute(query, (start, end))

    #print(cursor.fetchall())
    result_query = cursor.fetchall()

    group, value = '', 0
    for t in result_query:
        group, value = t

        if (len(group) < 25):
            tam = 25 - len(group)
            print(f"{group}{tam * ' '}R${value}")
'''



'''Recebe entrada do usuário e padroniza a mesma'''
def format_string_date(day):
    aux = ''

    for i in day:
        if(i != '/'):
            aux += i
        else:
            aux += '-'

    aux = datetime.strptime(aux, '%d-%m-%Y').date()
    return(aux)


'''Interface de interação com o usuário'''
def start():
    print(PySide6.__version__)
    print(PySide6.QtCore.__version__)

    print('Bem-vindo!\n' +
          'Informe o período de abrangência do relatório')

    first_day = input('Data inicial: ')
    first_day = format_string_date(first_day)

    last_day = input('Data final: ')
    last_day = format_string_date(last_day)

    generate_report(first_day, last_day)