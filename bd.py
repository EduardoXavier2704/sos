def insert(mydb, Nome, Cpf, Data_nasc, Email, Endereco, Lugar_referencia):
    mycursor = mydb.cursor()

    sql = "INSERT INTO ocorrencia (Nome, Cpf, Data_nasc, Email, Endereco, Lugar_referencia) VALUES (%s, %s, %s, %s, %s, %s)"
    val = (Nome, Cpf, Data_nasc, Email, Endereco, Lugar_referencia)

    mycursor.execute(sql, val)

    mydb.commit()

    print(mycursor.rowcount, "Inserido com Sucesso.")

    mycursor.close()

def insert(mydb, Nome_completo_proximo, Cpf_proximo, Data_nasc_proximo, Email_proximo, Endereco_proximo, Local_referencia):
    mycursor = mydb.cursor()

    sql = "INSERT INTO ocorrencia_proximo (Nome_completo_proximo, Cpf_proximo, Data_nasc_proximo, Email_proximo, Endereco_proximo, Local_referencia) VALUES (%s, %s, %s, %s, %s, %s)"
    val = (Nome_completo_proximo, Cpf_proximo, Data_nasc_proximo, Email_proximo, Endereco_proximo, Local_referencia)

    mycursor.execute(sql, val)

    mydb.commit()

    print(mycursor.rowcount, "Inserido com Sucesso.")

    mycursor.close()

def update(mydb, titulo_antigo, titulo_novo, autor, ano, status_):
    mycursor = mydb.cursor()

    sql = "UPDATE livros SET titulo = %s, autor = %s, ano = %s, status_ = %s WHERE titulo = %s"
    val = (titulo_novo, autor, ano, status_, titulo_antigo)

    mycursor.execute(sql, val)

    mydb.commit()

    print(mycursor.rowcount, "registro(s) atualizado(s).")

    mycursor.close()


def delete(mydb, titulo):
    mycursor = mydb.cursor()

    sql = "DELETE FROM livros WHERE titulo = %s"
    val = (titulo,)

    mycursor.execute(sql, val)

    mydb.commit()

    print(mycursor.rowcount, "registro(s) excluído(s).")

    mycursor.close()



def query(mydb):
    mycursor = mydb.cursor()

    sql = "SELECT titulo, autor, ano, status_ FROM livros"
    mycursor.execute(sql)

    rows = mycursor.fetchall()

    # Cria uma lista vazia para armazenar os dados
    dados = []

    # Itera sobre cada linha retornada pela consulta e adiciona os dados formatados à lista
    for row in rows:
        # Verifica se o valor é None antes de formatá-lo na string de impressão
        titulo = row[0] if row[0] is not None else ""
        autor = row[1] if row[1] is not None else ""
        ano = row[2] if row[2] is not None else ""
        status_ = "Disponível" if row[3] else "Indisponível" if row[3] is not None else ""

        dados.append("{: <20} {: <30} {: <10} {: <10}".format(
            titulo, autor, ano, status_))

    # Retorna a lista de dados
    return dados

def register(mydb, nome, email, celular, senha):
    mycursor = mydb.cursor()

    sql = "INSERT INTO registro_usuario (nome, email, celular, senha) VALUES (%s, %s, %s, %s)"
    val = (nome, email, celular, senha)

    mycursor.execute(sql, val)

    mydb.commit()

    print("Usuário registrado com sucesso.")

    mycursor.close()


def login(mydb, nome, senha):
    mycursor = mydb.cursor()

    sql = "SELECT * FROM registro_usuario WHERE nome = %s AND senha = %s"
    val = (nome, senha)

    mycursor.execute(sql, val)

    user = mycursor.fetchone()

    if user:
        print("Login bem-sucedido.")
        return user
    else:
        print("Credenciais inválidas.")
        return None


