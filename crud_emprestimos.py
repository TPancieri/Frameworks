from library import *
from library.funcionario import Funcionario
from crud_livros import buscar_livro_por_titulo_ou_isbn
from crud_clientes import buscar_cliente_por_nome_ou_email
from datetime import datetime, timedelta

def validar_data_devolucao(data_str):
    """Valida e converte a string da data para datetime"""
    try:
        data = datetime.strptime(data_str, '%d/%m/%Y')
        if data.date() < datetime.now().date():
            raise ValueError("A data de devolução não pode ser no passado")
        return data
    except ValueError as e:
        if str(e) == "A data de devolução não pode ser no passado":
            raise e
        raise ValueError("Data inválida. Use o formato DD/MM/AAAA")

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
    
    while True:
        data_devolucao = input("\nData prevista para devolução (DD/MM/AAAA): ")
        try:
            data_prevista = validar_data_devolucao(data_devolucao)
            break
        except ValueError as e:
            print(f"Erro: {str(e)}")
            if input("Deseja tentar novamente? (s/n): ").lower() != 's':
                print("Empréstimo cancelado.")
                input("Pressione Enter para continuar.")
                return
    
    confirmacao = input(f"\nConfirmar empréstimo até {data_prevista.strftime('%d/%m/%Y')}? (s/n): ").lower()
    if confirmacao != 's':
        print("Empréstimo cancelado.")
        input("Pressione Enter para continuar.")
        return
    
    try:
        Funcionario().registrar_emprestimo(cliente.id, livro.isbn, data_prevista)
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
        status = "ATRASADO" if emp.esta_atrasado() else "No prazo"
        print(f"{i}. {emp.livro.titulo} (ISBN: {emp.livro.isbn})")
        print(f"   Emprestado em: {emp.data_emprestimo.strftime('%d/%m/%Y %H:%M')}")
        print(f"   Devolver até: {emp.data_prevista_devolucao.strftime('%d/%m/%Y')}")
        print(f"   Status: {status}")
    
    try:
        escolha = int(input("\nEscolha o número do livro a devolver: "))
        if escolha < 1 or escolha > len(emprestimos_ativos):
            print("Opção inválida.")
            input("Pressione Enter para continuar.")
            return
        
        emprestimo = emprestimos_ativos[escolha - 1]
        
        if emprestimo.esta_atrasado():
            print("\nATENÇÃO: Este livro está com a devolução atrasada!")
        
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
