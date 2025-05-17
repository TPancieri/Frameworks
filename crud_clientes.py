from library import *
from library.cliente import Cliente
from library.funcionario import Funcionario

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

def buscar_cliente_por_nome_ou_email(termo):
    return (Cliente
            .select()
            .where(
                (Cliente.nome.contains(termo)) | 
                (Cliente.email.contains(termo))
            )
            .first()) 
