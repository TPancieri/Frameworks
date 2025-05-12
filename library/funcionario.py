from .usuario import Usuario
from .cliente import Cliente
from .livro import Livro
from .emprestimo import Emprestimo
from datetime import datetime
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
    
    def atualizar_status_livro(self, isbn, disponivel):
            livro = Livro.get_or_none(Livro.isbn == isbn)
            if livro:
                livro.disponivel = disponivel
                livro.save()
            else:
                raise ValueError("Livro não encontrado.")
    
    def registrar_emprestimo(self, id_usuario, isbn):
        livro = Livro.get_or_none(Livro.isbn == isbn)
        usuario = Cliente.get_or_none(Cliente.id == id_usuario)

        if not livro or not usuario:
            raise ValueError("Livro ou usuário não encontrado.")
        if not livro.disponivel:
            raise ValueError("Livro já está emprestado.")

        Emprestimo.create(livro=livro, usuario=usuario)
        livro.disponivel = False
        livro.save()

    def registrar_devolucao(self, id_emprestimo):
        emprestimo = Emprestimo.get_or_none(Emprestimo.id == id_emprestimo)
        if not emprestimo:
            raise ValueError("Empréstimo não encontrado.")
        if emprestimo.status == 'devolvido':
            raise ValueError("Esse livro já foi devolvido.")

        emprestimo.status = 'devolvido'
        emprestimo.data_devolucao = datetime.now()
        emprestimo.save()

        livro = emprestimo.livro
        livro.disponivel = True
        livro.save()

#TODO mudar logica de emprestimo, mostrar qual livro esta com quem no listar livros e quais livros alguem tem no listar clientes, nao fazer atualizacao por ID de emprestimo mas por alguma outra coisa (ISBN?)
