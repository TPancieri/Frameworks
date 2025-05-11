from .usuario import Usuario
from .cliente import Cliente
from .livro import Livro
from peewee import *

class Funcionario(Usuario):
    class Meta:
        table_name = 'funcionario'

    def ver_clientes(self):
        return Cliente.select()

    def cadastrar_cliente(self, nome, cpf, email, telefone):
        return Cliente.create(
            nome=nome,
            cpf=cpf,
            email=email,
            telefone=telefone,
            tipo='cliente'
        )

    def atualizar_cliente(self, cliente_id, **data):
        query = Cliente.update(**data).where(Cliente.id == cliente_id)
        return query.execute()

    def deletar_cliente(self, cliente_id):
        return Cliente.delete_by_id(cliente_id)

    def ver_livros(self):
        return Livro.select()

    def cadastrar_livro(self, isbn, titulo, autor, editora, ano_publicacao, genero):
        return Livro.create(
            isbn=isbn,
            titulo=titulo,
            autor=autor,
            editora=editora,
            ano_publicacao=ano_publicacao,
            genero=genero,
            disponivel=True
        )

    def atualizar_livro(self, isbn, **data):
        query = Livro.update(**data).where(Livro.isbn == isbn)
        return query.execute()

    def deletar_livro(self, isbn):
        return Livro.delete().where(Livro.isbn == isbn).execute()
