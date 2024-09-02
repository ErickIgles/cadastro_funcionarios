import  mysql.connector
from datetime import date
from time import sleep

def connection():
    """
    Makes the connection to the database.
    """
    
    try:
        conn = mysql.connector.connect(
            database='empresato',
            host='localhost',
            user='erick', # conection name
            passwd='jacadoamanhecer741@'
        )
        return conn
    except mysql.connector.Error as err:
        print(f'Error connecting to Mysql server: {err}')


def disconnect(conn):
    """
    disconnect the database

    "conn" is the database connection parameter and therefore a disconnect is returned
    """
    if conn:
        conn.close()


def list_employees():
    """
    function to list employees.
    """
    conn = connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM funcionarios")
    funcionarios = cursor.fetchall()

    if len(funcionarios) > 0:
        for fun in funcionarios:
            print(f'COD:{fun[0]}')
            print(f'NOME:{fun[1]}')
            print(f'DATA DE NASCIMENTO:{fun[2]}')
            print(f'CPF:{fun[3]}')
            print(f'ENDEREÇO:{fun[4]}')
            print(f'TELEFONE:{fun[5]}')
            print(f'E-MAIL:{fun[6]}')
            print(f'DATA DE ADMISSÃO:{fun[7]}')

    else:
        print('Não há funcionarios cadastrados.')    
    disconnect(conn)



def create_employee():
    """
    function to create employee.
    """
    conn = connection()
    cursor = conn.cursor()

    nome = input('Nome do funcionário: ')
    data_nascimento = input('Data de nascimento: ')
    cpf = input('CPF:')
    endereco = input('Endereço: ')
    telefone = input('Telefone: ')
    email = input('Email: ')
    data_admissao = date.today()
    id_cargo = int(input('ID do cargo: '))
    id_departamento = int(input('ID do departemento: '))

    query = "INSERT INTO funcionarios (nome, data_nascimento, cpf, endereco, telefone, email, data_admissao, id_cargo, id_departamento) VALUES(%s, %s , %s, %s, %s, %s, %s, %s, %s)"
    cursor.execute(query, (nome, data_nascimento, cpf, endereco, telefone, email, data_admissao, id_cargo, id_departamento))
    conn.commit()

    if cursor.rowcount == 1:
        print(f'O funcionário {nome} foi cadastrado com sucesso!')
    else:
        print('Erro ao cadastrar o funcionário.')
    disconnect(conn)


def update_employee():
    conn = connection()
    cursor = conn.cursor()

    query = 'SELECT * FROM funcionarios'
    cursor.execute(query)
    funcionarios = cursor.fetchall()

    if len(funcionarios) > 0:   

        codigo = int(input('Código do funcionário: '))

        query = 'SELECT * FROM funcionarios WHERE codigo_funcionario=%s'
        cursor.execute(query, (codigo,))
        funcionario = cursor.fetchall()

        if len(funcionario) > 0:

            nome = input('Nome do funcionário: ')
            data_nascimento = input('Data de nascimento: ')
            cpf = input('CPF:')
            endereco = input('Endereço: ')
            telefone = input('Telefone: ')
            email = input('Email: ')
            id_cargo = int(input('ID do cargo: '))
            id_departamento = int(input('ID do departemento: '))

            query = 'UPDATE funcionarios SET nome=%s, data_nascimento=%s, cpf=%s, endereco=%s, telefone=%s, email=%s, id_cargo=%s, id_departamento=%s WHERE codigo_funcionario=%s'
            
            cursor.execute(query, (nome, data_nascimento, cpf, endereco, telefone, email, id_cargo, id_departamento, codigo))
            conn.commit()

            if cursor.rowcount == 1:
                print(f'Os dados do funcionário {nome} foram atualizado com sucesso.')
            else:
                print('Erro ao atualizar o funcionário.')
        else:
            print(f'Não há funcionário com esse código: {codigo}')
    else:
        print('Não há funcionários cadastrados.')
    disconnect(conn)




def delete_employee():
    """
    function to delete employee.
    """

    conn = connection()
    cursor = conn.cursor()

    query = 'SELECT * FROM funcionarios'
    cursor.execute(query)
    funcionarios = cursor.fetchall()
    
    if len(funcionarios) > 0:


        codigo = int(input('Código do funcionário: '))

        query = "DELETE FROM funcionarios WHERE codigo_funcionario=%s"
        cursor.execute(query, (codigo,))
        conn.commit()

        if cursor.rowcount == 1:
            print(f'O funcionário foi deletado com sucesso.')
        else:
            print('Erro ao deletar o funcionário.')
    else:
        print('Não há funcionários cadastrados.')
    disconnect(conn)


def menu():
    print('-------------------------------')
    print('MENU DE CADASTRO DE FUNCIONÁRIO')
    print('-------------------------------')
    print('COD: 01 - CADASTRO DE FUNCIONÁRIO')
    print('COD: 02 - ATUALIZAR DADOS DO FUNCIONÁRIO')
    print('COD: 03 - DELETAR FUNCIONÁRIO')
    print('COD: 04 - LISTAR FUNCIONÁRIOS')
    print('COD: 05 - ENCERRAR PROGRAMA')

    op = int(input('Informe o código do processo: '))

    if op in (1, 2, 3, 4, 5):
        if op == 1:
            create_employee()
        elif op == 2:
            update_employee()
        elif op == 3:
            delete_employee()
        elif op == 4:
            list_employees()
        elif op == 5:
            print('Encerrando o programa...')
            sleep(1)
        else:
            print('Valor informado inválido!')

    else:
        print('Valor informado inválido!')

