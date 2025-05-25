from library import *
from library.cliente import Cliente
from library.funcionario import Funcionario
from datetime import datetime

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
                status = "ATRASADO" if emprestimo.esta_atrasado() else "No prazo"
                print(f"    - {emprestimo.livro.titulo} (ISBN: {emprestimo.livro.isbn})")
                print(f"      Emprestado em: {emprestimo.data_emprestimo.strftime('%d/%m/%Y %H:%M')}")
                print(f"      Devolver até: {emprestimo.data_prevista_devolucao.strftime('%d/%m/%Y')}")
                print(f"      Status: {status}")
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

def listar_emprestimos_ativos():
    print("\n--- EMPRÉSTIMOS ATIVOS ---")
    
    emprestimos = (Emprestimo
                  .select()
                  .where(Emprestimo.status == 'emprestado')
                  .order_by(Emprestimo.data_prevista_devolucao))
    
    if not emprestimos:
        print("Não há empréstimos ativos no momento.")
        input("\nPressione Enter para voltar ao menu.")
        return
    
    print(f"\nTotal de empréstimos ativos: {len(emprestimos)}")
    for emp in emprestimos:
        try:
            status = "ATRASADO" if emp.esta_atrasado() else "No prazo"
            print(f"\nLivro: {emp.livro.titulo} (ISBN: {emp.livro.isbn})")
            print(f"Cliente: {emp.usuario.nome} (ID: {emp.usuario.id})")
            print(f"Data do empréstimo: {emp.data_emprestimo.strftime('%d/%m/%Y %H:%M')}")
            print(f"Data prevista de devolução: {emp.data_prevista_devolucao.strftime('%d/%m/%Y')}")
            print(f"Status: {status}")
            if emp.esta_atrasado():
                dias_atraso = (datetime.now() - emp.data_prevista_devolucao).days
                print(f"Dias de atraso: {dias_atraso}")
            print("-" * 50)
        except Exception as e:
            print(f"[ERRO ao exibir empréstimo: {str(e)}]")
            print("-" * 50)
    
    input("\nPressione Enter para voltar ao menu.")

def listar_clientes_atrasados():
    print("\n--- CLIENTES COM EMPRÉSTIMOS ATRASADOS ---")
    
    # Busca empréstimos atrasados
    emprestimos_atrasados = (Emprestimo
                           .select()
                           .where(
                               (Emprestimo.status == 'emprestado') &
                               (Emprestimo.data_prevista_devolucao < datetime.now())
                           )
                           .order_by(Emprestimo.data_prevista_devolucao))
    
    if not emprestimos_atrasados:
        print("Não há empréstimos atrasados no momento.")
        input("\nPressione Enter para voltar ao menu.")
        return
    
    # Agrupa empréstimos por cliente
    clientes_atrasados = {}
    for emp in emprestimos_atrasados:
        try:
            cliente_id = emp.usuario.id
            if cliente_id not in clientes_atrasados:
                clientes_atrasados[cliente_id] = {
                    'cliente': emp.usuario,
                    'emprestimos': []
                }
            
            dias_atraso = (datetime.now() - emp.data_prevista_devolucao).days
            clientes_atrasados[cliente_id]['emprestimos'].append({
                'livro': emp.livro,
                'data_prevista': emp.data_prevista_devolucao,
                'dias_atraso': dias_atraso
            })
        except Exception as e:
            print(f"[ERRO ao processar empréstimo: {str(e)}]")
    
    # Exibe os resultados
    print(f"\nTotal de clientes com atrasos: {len(clientes_atrasados)}")
    for cliente_id, dados in clientes_atrasados.items():
        try:
            cliente = dados['cliente']
            print(f"\nCliente: {cliente.nome} (ID: {cliente.id})")
            print(f"Email: {cliente.email}")
            print(f"Telefone: {cliente.telefone}")
            print("\nLivros atrasados:")
            for emp in dados['emprestimos']:
                print(f"  - {emp['livro'].titulo} (ISBN: {emp['livro'].isbn})")
                print(f"    Devolver até: {emp['data_prevista'].strftime('%d/%m/%Y')}")
                print(f"    Dias em atraso: {emp['dias_atraso']}")
            print("-" * 50)
        except Exception as e:
            print(f"[ERRO ao exibir cliente: {str(e)}]")
            print("-" * 50)
    
    input("\nPressione Enter para voltar ao menu.") 
