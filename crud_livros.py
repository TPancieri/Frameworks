from library import *
from library.livro import Livro
from library.funcionario import Funcionario

def listar_livros():
    print("\n--- LIVROS CADASTRADOS ---")
    for livro in Livro.select():
        status = 'Disponível' if livro.disponivel else 'Emprestado'
        print(f"{livro.isbn} - {livro.titulo}")
        print(f"    Status: {status}")
        print("-" * 50)
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

def buscar_livro_por_titulo_ou_isbn(termo):
    return (Livro
            .select()
            .where(
                (Livro.titulo.contains(termo)) | 
                (Livro.isbn.contains(termo))
            )
            .first()) 
