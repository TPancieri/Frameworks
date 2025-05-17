from library import *
from library.livro import Livro
from library.funcionario import Funcionario

def listar_livros():
    print("\n--- LIVROS CADASTRADOS ---")
    for livro in Livro.select():
        emprestimo_atual = None
        if not livro.disponivel:
            try:
                emprestimo_atual = (Emprestimo
                                .select().where(
                                    (Emprestimo.livro == livro) & 
                                    (Emprestimo.status == 'emprestado')
                                ).first())
            except Exception:
                emprestimo_atual = None
            
        status = 'Disponível' if livro.disponivel else 'Emprestado'
        
        if emprestimo_atual:
            try:
                print(f"{livro.isbn} - {livro.titulo}")
                print(f"    Status: {status}")
                print(f"    Emprestado para: {emprestimo_atual.usuario.nome} (ID: {emprestimo_atual.usuario.id})")
                print(f"    Data do empréstimo: {emprestimo_atual.data_emprestimo.strftime('%d/%m/%Y %H:%M')}")
            except Exception:
                print(f"{livro.isbn} - {livro.titulo}")
                print(f"    Status: {status}")
                print(f"    ERRO: Dados do usuário não encontrados")
        else:
            print(f"{livro.isbn} - {livro.titulo} ({status})")
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
