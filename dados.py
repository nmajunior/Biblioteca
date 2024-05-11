import sqlite3

#Criar ou contectar ao banco de dados
con = sqlite3.connect('biblioteca.db')
#cursor = con.cursor

#Criar Tabela de Livros
con.execute('''CREATE TABLE IF NOT EXISTS livros(
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            titulo TEXT,
            autor TEXT,
            editora TEXT,
            ano_publicacao INTEGER,
            isbn TEXT)''')
#con.commit()

#Criar tabela de Usuarios
con.execute('''CREATE TABLE IF NOT EXISTS usuarios(
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            sobrenome TEXT,
            endereco TEXT,
            email TEXT,
            telefone TEXT)''')
#con.commit()

#Criar tabela de emprestimo

con.execute('''CREATE TABLE IF NOT EXISTS emprestimos(
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            id_livro INTEGER,
            id_usuario INTEGER,
            data_emprestimo TEXT,
            data_devolucao TEXT,
            FOREIGN KEY(id_livro) REFERENCES livros(id),
            FOREIGN KEY(id_usuario) REFERENCES usuarios(id))''')
#con.commit()
