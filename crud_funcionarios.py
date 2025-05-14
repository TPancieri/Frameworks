"""
Interface das operações CRUD do funcionario
"""
from library import *
from library.livro import Livro
from library.cliente import Cliente
from library.funcionario import Funcionario

def listar_livros():
    print("\n--- LIVROS CADASTRADOS ---")
    for livro in Livro.select():
        print(f"{livro.isbn} - {livro.titulo} ({'Disponível' if livro.disponivel else 'Emprestado'})")
    input("\nPressione Enter para voltar ao menu.")

def cadastrar_livro():
    print("\n--- CADASTRAR LIVRO ---")
    isbn = input("ISBN: ")
    titulo = input("Título: ")
    autor = input("Autor: ")
    editora = input("Editora: ")
    ano = int(input("Ano de publicação: "))
    genero = input("Gênero: ")

    try:
        Funcionario().cadastrar_livro(isbn, titulo, autor, editora, ano, genero)
        print("Livro cadastrado com sucesso.")
    except Exception as e:
        print("Erro ao cadastrar livro:", e)
    input("Pressione Enter para continuar.")

def atualizar_livro():
    print("\n--- ATUALIZAR LIVRO ---")
    isbn = input("ISBN do livro a atualizar: ")
    campo = input("Campo a atualizar (titulo, autor, editora, ano_publicacao, genero): ")
    valor = input("Novo valor: ")

    try:
        Funcionario().atualizar_livro(isbn, **{campo: valor})
        print("Livro atualizado com sucesso.")
    except Exception as e:
        print("Erro ao atualizar livro:", e)
    input("Pressione Enter para continuar.")

def deletar_livro():
    print("\n--- DELETAR LIVRO ---")
    isbn = input("ISBN do livro a deletar: ")
    try:
        Funcionario().deletar_livro(isbn)
        print("Livro deletado com sucesso.")
    except Exception as e:
        print("Erro ao deletar livro:", e)
    input("Pressione Enter para continuar.")

def listar_clientes():
    print("\n--- CLIENTES CADASTRADOS ---")
    for cliente in Cliente.select():
        print(f"{cliente.id} - {cliente.nome} ({cliente.email})")
    input("\nPressione Enter para voltar ao menu.")

def cadastrar_cliente():
    print("\n--- CADASTRAR CLIENTE ---")
    nome = input("Nome: ")
    cpf = input("CPF: ")
    email = input("Email: ")
    telefone = input("Telefone: ")

    try:
        Funcionario().cadastrar_cliente(nome, cpf, email, telefone)
        print("Cliente cadastrado com sucesso.")
    except Exception as e:
        print("Erro ao cadastrar cliente:", e)
    input("Pressione Enter para continuar.")

def atualizar_cliente():
    print("\n--- ATUALIZAR CLIENTE ---")
    id_cliente = input("ID do cliente: ")
    campo = input("Campo a atualizar (nome, cpf, email, telefone): ")
    valor = input("Novo valor: ")

    try:
        Funcionario().atualizar_cliente(id_cliente, **{campo: valor})
        print("Cliente atualizado com sucesso.")
    except Exception as e:
        print("Erro ao atualizar cliente:", e)
    input("Pressione Enter para continuar.")

def deletar_cliente():
    print("\n--- DELETAR CLIENTE ---")
    id_cliente = input("ID do cliente: ")
    try:
        Funcionario().deletar_cliente(id_cliente)
        print("Cliente deletado com sucesso.")
    except Exception as e:
        print("Erro ao deletar cliente:", e)
    input("Pressione Enter para continuar.")

def emprestar_livro():
    print("\n--- EMPRESTAR LIVRO ---")
    id_usuario = input("ID do cliente: ")
    isbn = input("ISBN do livro: ")
    try:
        Funcionario().registrar_emprestimo(id_usuario, isbn)
        print("Livro emprestado com sucesso.")
    except Exception as e:
        print("Erro ao emprestar livro:", e)
    input("Pressione Enter para continuar.")

def devolver_livro():
    print("\n--- DEVOLVER LIVRO ---")
    id_emprestimo = input("ID do empréstimo: ")
    try:
        Funcionario().registrar_devolucao(id_emprestimo)
        print("Livro devolvido com sucesso.")
    except Exception as e:
        print("Erro ao devolver livro:", e)
    input("Pressione Enter para continuar.")
