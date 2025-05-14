"""
Inicialização do script, cria todos os indexes e tabelas necessárias para o db.
Roda uma vez quando preparando o programa pela primeira vez
"""
from library.config import db
from library.livro import Livro
from library.usuario import Usuario
from library.cliente import Cliente
from library.funcionario import Funcionario
from library.emprestimo import Emprestimo

if __name__ == '__main__':
    db.connect()
    db.create_tables([Livro, Usuario, Cliente, Funcionario, Emprestimo])
    db.close()
