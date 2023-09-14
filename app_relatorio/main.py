'''
    Filename: main.py
    Author: izahterencio@gmail.com
    Date: 2023/09/04
'''


'''Função responsável por realizar a conexão com o banco de dados do sistema'''
def connect_database(name, usr, passwd):


def generate_report(start, end):
    query = ("SELECT GRUPO.descricao AS GRUPO, "
             "SUM((ITEM.vlr_total + ITEM.vlr_despesa - ITEM.vlr_desc)) AS VAL_VENDIDO "
             "FROM tb_est_grupo AS GRUPO, tb_estoque AS ESTOQUE, tb_nfv_item AS ITEM, "
             "tb_est_identificador AS ESTOQUE_ID, tb_nfvenda AS VENDA "
             "WHERE GRUPO.id_grupo IS NOT NULL AND GRUPO.id_grupo = ESTOQUE.id_grupo AND ESTOQUE.id_estoque = "
             "ESTOQUE_ID.id_estoque AND ESTOQUE_ID.id_identificador = ITEM.id_identificador AND ITEM.id_nfvenda = "
             "VENDA.id_nfvenda AND VENDA.dt_emissao BETWEEN " + start + " AND " + end + " GROUP BY GRUPO.descricao")

# realiza a query
# acessa o banco de dados
# exibe o resultado ao usuário


'''Recebe entrada do usuário e padroniza a mesma'''
def format_string_date(day):
    aux = ''

    for i in day:
        if(i != '/'):
            aux += i
        else:
            aux += '-'

    return(aux)


'''Interface de interação com o usuário'''
def start():
    print('Bem-vindo!\n' +
          'Informe o período de abrangência do relatório')

    first_day = input('Data inicial: ')
    first_day = format_string_date(first_day)

    last_day = input('Data final: ')
    last_day = format_string_date(last_day)

    generate_report(first_day, last_day)


    # chama função gerar relatório passando a data


# Call the user interactive  function
if __name__ == '__main__':
    start()