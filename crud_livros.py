from library import *
from library.livro import Livro
from library.funcionario import Funcionario
from library.emprestimo import Emprestimo

def listar_livros():
    print("\n--- LIVROS CADASTRADOS ---")
    for livro in Livro.select():
        status = 'Disponível' if livro.disponivel else 'Emprestado'
        print(f"{livro.isbn} - {livro.titulo}")
        print(f"    Autor: {livro.autor}")
        print(f"    Editora: {livro.editora}")
        print(f"    Ano: {livro.ano_publicacao}")
        print(f"    Gênero: {livro.genero}")
        print(f"    Status: {status}")
        
        if not livro.disponivel:
            try:
                # Busca o empréstimo ativo deste livro
                emprestimo = (Emprestimo
                            .select()
                            .where(
                                (Emprestimo.livro == livro) & 
                                (Emprestimo.status == 'emprestado')
                            )
                            .first())
                
                if emprestimo:
                    try:
                        usuario = emprestimo.usuario
                        status_emprestimo = "ATRASADO" if emprestimo.esta_atrasado() else "No prazo"
                        print(f"    Emprestado para: {usuario.nome}")
                        print(f"    Devolver até: {emprestimo.data_prevista_devolucao.strftime('%d/%m/%Y')}")
                        print(f"    Status do empréstimo: {status_emprestimo}")
                    except Usuario.DoesNotExist:
                        print("    [ERRO: Usuário do empréstimo não encontrado]")
                        print("    [Este empréstimo precisa ser corrigido no banco de dados]")
            except Exception as e:
                print(f"    [ERRO ao buscar informações do empréstimo: {str(e)}]")
        
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

def buscar_livros():
    print("\n--- BUSCAR LIVROS ---")
    print("1. Buscar por título")
    print("2. Buscar por autor")
    print("3. Buscar por gênero")
    print("4. Buscar por qualquer critério")
    
    opcao = input("\nEscolha o tipo de busca: ")
    
    if opcao not in ['1', '2', '3', '4']:
        print("Opção inválida!")
        input("Pressione Enter para continuar.")
        return
    
    termo = input("\nDigite o termo de busca: ").strip()
    if not termo:
        print("Termo de busca não pode ser vazio!")
        input("Pressione Enter para continuar.")
        return
    
    try:
        if opcao == '1':
            livros = Livro.select().where(Livro.titulo.contains(termo))
        elif opcao == '2':
            livros = Livro.select().where(Livro.autor.contains(termo))
        elif opcao == '3':
            livros = Livro.select().where(Livro.genero.contains(termo))
        else:  # opcao 4 - busca em todos os campos
            livros = (Livro
                     .select()
                     .where(
                         (Livro.titulo.contains(termo)) |
                         (Livro.autor.contains(termo)) |
                         (Livro.genero.contains(termo))
                     ))
        
        if not livros:
            print("\nNenhum livro encontrado com os critérios informados.")
            input("Pressione Enter para continuar.")
            return
        
        print(f"\nEncontrados {len(livros)} livro(s):")
        for livro in livros:
            status = 'Disponível' if livro.disponivel else 'Emprestado'
            print(f"\n{livro.isbn} - {livro.titulo}")
            print(f"    Autor: {livro.autor}")
            print(f"    Editora: {livro.editora}")
            print(f"    Ano: {livro.ano_publicacao}")
            print(f"    Gênero: {livro.genero}")
            print(f"    Status: {status}")
            
            if not livro.disponivel:
                try:
                    emprestimo = (Emprestimo
                                .select()
                                .where(
                                    (Emprestimo.livro == livro) & 
                                    (Emprestimo.status == 'emprestado')
                                )
                                .first())
                    
                    if emprestimo:
                        try:
                            usuario = emprestimo.usuario
                            status_emprestimo = "ATRASADO" if emprestimo.esta_atrasado() else "No prazo"
                            print(f"    Emprestado para: {usuario.nome}")
                            print(f"    Devolver até: {emprestimo.data_prevista_devolucao.strftime('%d/%m/%Y')}")
                            print(f"    Status do empréstimo: {status_emprestimo}")
                        except Usuario.DoesNotExist:
                            print("    [ERRO: Usuário do empréstimo não encontrado]")
                except Exception as e:
                    print(f"    [ERRO ao buscar informações do empréstimo: {str(e)}]")
            
            print("-" * 50)
            
    except Exception as e:
        print(f"Erro ao buscar livros: {str(e)}")
    
    input("\nPressione Enter para voltar ao menu.")

def buscar_livro_por_titulo_ou_isbn(termo):
    return (Livro
            .select()
            .where(
                (Livro.titulo.contains(termo)) | 
                (Livro.isbn.contains(termo))
            )
            .first()) 
