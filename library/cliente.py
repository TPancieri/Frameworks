"""
Modulo do cliente
"""

from .usuario import Usuario
from .livro import Livro
from .emprestimo import Emprestimo
from peewee import *
from datetime import datetime

class Cliente(Usuario):
    """
    Inherit do Usuário 

    Operações:
    - Pegar livro emprestado
    - Retornar livros
    - Ver os livros disponiveis
    - Update na informação pessoal
    """
    class Meta:
        table_name = 'cliente'

    def pedir_livro(self, livro):
        if not livro.disponivel:
            raise ValueError("Livro indisponível")
        emprestimo = Emprestimo.create(
            livro=livro,
            usuario=self,
            status='emprestado'
        )
        livro.disponivel = False
        livro.save()
        return emprestimo

    def conferir_livros_disponiveis(self):
        return Livro.select().where(Livro.disponivel == True)

    def devolver_livro(self, emprestimo):
        if emprestimo.status != 'emprestado':
            raise ValueError("Empréstimo já devolvido")
        emprestimo.status = 'devolvido'
        emprestimo.data_devolucao = datetime.now()
        emprestimo.save()
        livro = emprestimo.livro
        livro.disponivel = True
        livro.save()
        return emprestimo

    def atualizar_informacoes(self, nome=None, cpf=None, email=None, telefone=None):
        if nome:
            self.nome = nome
        if cpf:
            self.cpf = cpf
        if email:
            self.email = email
        if telefone:
            self.telefone = telefone
        self.save()
