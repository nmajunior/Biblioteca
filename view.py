import sqlite3


def conect():
    #Criar ou contectar ao banco de dados
    conn = sqlite3.connect('biblioteca.db')
    return conn

#Função para inserir um novo livro

def inserir_livro(titulo, autor, editora, ano_publicacao, isbn):
    conn = conect()
    conn.execute('INSERT INTO livros(titulo, autor, editora, ano_publicacao, isbn) VALUES( ?,?,?,?,?)', (titulo, autor, editora, ano_publicacao, isbn))
    conn.commit()


#Inserir Usuarios
def inserir_usuarios(nome, sobrenome, endereco, email, telefone):
    conn = conect()
    conn.execute('INSERT INTO usuarios(nome, sobrenome, endereco, email, telefone) VALUES(?,?,?,?,?)', (nome, sobrenome, endereco, email, telefone))
    conn.commit()


#Função para exibir livros
def exibir_livros():
    conn = conect()
    livros = conn.execute('SELECT * FROM livros').fetchall()
    conn.close()

    if not livros:
        print('Nenhum Livro encontrado')
        return
    else:
        print('Livros na Biblioteca: ')
        for livro in livros:
            print('='*10)
            print(f'ID : {livro[0]}')
            print(f'Título : {livro[1]}')
            print(f'Autor : {livro[2]}')
            print(f'Editora : {livro[3]}')
            print(f'Ano de Publicação : {livro[4]}')
            print(f'ISBN : {livro[5]}')
            print('='*10)
            print('')



#Função para realizar emprestimo
def adicionar_emprestimo(id_livro, id_usuario, data_emprestimo, data_devolucao):
    conn = conect()
    conn.execute('INSERT INTO emprestimos(id_livro, id_usuario, data_emprestimo, data_devolucao) VALUES(?,?,?,?)', (id_livro, id_usuario, data_emprestimo, data_devolucao))
    conn.commit()
    conn.close()

#Função para exibir livros emprestados no momento
def livros_emprestados():
    conn = conect()
    result = conn.execute('SELECT emprestimos.id, livros.titulo, usuarios.nome, usuarios.sobrenome,  emprestimos.data_emprestimo, emprestimos.data_devolucao FROM livros INNER JOIN emprestimos ON livros.id = emprestimos.id_livro INNER JOIN usuarios ON usuarios.id = emprestimos.id_usuario WHERE emprestimos.data_devolucao IS NULL').fetchall()
    conn.close()
    return result

#Função para atualizar a data de devolução do livro emprestado
def atualiza_data_de_devolucao_do_livro(id_emprestimo, data_devolucao):
    conn = conect()
    conn.execute('UPDATE emprestimos SET data_devolucao = ? WHERE id = ?', (id_emprestimo, data_devolucao) )
    conn.commit()
    conn.close()
    



#testar função

#inserir_usuarios('Fudencio', 'da Silva','Rua do Brega 69', 'eu@vc.ocm', '123456')
#exibir_livros()
#adicionar_emprestimo(1,1,'2024-01-25',None)
emprestimo = livros_emprestados()
print(emprestimo)
#atualiza_data_de_devolucao_do_livro(1, '2024-02-20')