from library import *
from library.livro import Livro
from library.cliente import Cliente
from library.funcionario import Funcionario

#TODO breakdown em dois arquivos, um para funções de livro e outro para funções de cliente
#TODO talvez um historico de emprestimos por livro (contador de quantas vezes um livro foi emprestado, e para quem)?

def listar_livros():
    print("\n--- LIVROS CADASTRADOS ---")
    for livro in Livro.select():
        emprestimo_atual = None
        if not livro.disponivel:
            emprestimo_atual = (Emprestimo
                            .select().where(
                                (Emprestimo.livro == livro) & 
                                (Emprestimo.status == 'emprestado')
                            ).first())
            
        status = 'Disponível' if livro.disponivel else 'Emprestado'
        
        if emprestimo_atual:
            print(f"{livro.isbn} - {livro.titulo}")
            print(f"    Status: {status}")
            print(f"    Emprestado para: {emprestimo_atual.usuario.nome} (ID: {emprestimo_atual.usuario.id})")
            print(f"    Data do empréstimo: {emprestimo_atual.data_emprestimo.strftime('%d/%m/%Y %H:%M')}")
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

def listar_clientes():
    print("\n--- CLIENTES CADASTRADOS ---")
    for cliente in Cliente.select():
        print(f"\n{cliente.id} - {cliente.nome} ({cliente.email})")
        
        emprestimos_ativos = (Emprestimo
                            .select()
                            .where(
                                (Emprestimo.usuario == cliente) & 
                                (Emprestimo.status == 'emprestado')
                            ))
        
        if emprestimos_ativos:
            print("    Livros emprestados:")
            for emprestimo in emprestimos_ativos:
                print(f"    - {emprestimo.livro.titulo} (ISBN: {emprestimo.livro.isbn})")
                print(f"      Emprestado em: {emprestimo.data_emprestimo.strftime('%d/%m/%Y %H:%M')}")
        else:
            print("    Nenhum livro emprestado no momento")
        print("-" * 50)
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

def buscar_livro_por_titulo_ou_isbn(termo):
    return (Livro
            .select()
            .where(
                (Livro.titulo.contains(termo)) | 
                (Livro.isbn.contains(termo))
            )
            .first())

def buscar_cliente_por_nome_ou_email(termo):
    return (Cliente
            .select()
            .where(
                (Cliente.nome.contains(termo)) | 
                (Cliente.email.contains(termo))
            )
            .first())

def emprestar_livro():
    print("\n--- EMPRESTAR LIVRO ---")
    
    termo_cliente = input("Digite o nome ou email do cliente: ")
    cliente = buscar_cliente_por_nome_ou_email(termo_cliente)
    
    if not cliente:
        print("Cliente não encontrado.")
        input("Pressione Enter para continuar.")
        return
    
    print(f"\nCliente encontrado: {cliente.nome} (ID: {cliente.id})")
    
    termo_livro = input("\nDigite o título ou ISBN do livro: ")
    livro = buscar_livro_por_titulo_ou_isbn(termo_livro)
    
    if not livro:
        print("Livro não encontrado.")
        input("Pressione Enter para continuar.")
        return
    
    print(f"\nLivro encontrado: {livro.titulo} (ISBN: {livro.isbn})")
    
    if not livro.disponivel:
        print("Este livro já está emprestado.")
        input("Pressione Enter para continuar.")
        return
    
    confirmacao = input("\nConfirmar empréstimo? (s/n): ").lower()
    if confirmacao != 's':
        print("Empréstimo cancelado.")
        input("Pressione Enter para continuar.")
        return
    
    try:
        Funcionario().registrar_emprestimo(cliente.id, livro.isbn)
        print("Livro emprestado com sucesso.")
    except Exception as e:
        print("Erro ao emprestar livro:", e)
    input("Pressione Enter para continuar.")

def devolver_livro():
    print("\n--- DEVOLVER LIVRO ---")
    
    termo_cliente = input("Digite o nome ou email do cliente: ")
    cliente = buscar_cliente_por_nome_ou_email(termo_cliente)
    
    if not cliente:
        print("Cliente não encontrado.")
        input("Pressione Enter para continuar.")
        return
    
    print(f"\nCliente encontrado: {cliente.nome} (ID: {cliente.id})")
    
    emprestimos_ativos = (Emprestimo
                        .select()
                        .where(
                            (Emprestimo.usuario == cliente) & 
                            (Emprestimo.status == 'emprestado')
                        ))
    
    if not emprestimos_ativos:
        print("Este cliente não tem livros emprestados.")
        input("Pressione Enter para continuar.")
        return
    
    print("\nLivros emprestados:")
    for i, emp in enumerate(emprestimos_ativos, 1):
        print(f"{i}. {emp.livro.titulo} (ISBN: {emp.livro.isbn})")
        print(f"   Emprestado em: {emp.data_emprestimo.strftime('%d/%m/%Y %H:%M')}")
    
    try:
        escolha = int(input("\nEscolha o número do livro a devolver: "))
        if escolha < 1 or escolha > len(emprestimos_ativos):
            print("Opção inválida.")
            input("Pressione Enter para continuar.")
            return
        
        emprestimo = emprestimos_ativos[escolha - 1]
        
        confirmacao = input(f"\nConfirmar devolução de '{emprestimo.livro.titulo}'? (s/n): ").lower()
        if confirmacao != 's':
            print("Devolução cancelada.")
            input("Pressione Enter para continuar.")
            return
        
        Funcionario().registrar_devolucao(emprestimo.id)
        print("Livro devolvido com sucesso.")
    except ValueError:
        print("Por favor, digite um número válido.")
    except Exception as e:
        print("Erro ao devolver livro:", e)
    input("Pressione Enter para continuar.")
