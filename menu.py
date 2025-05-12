import os
from crud_funcionarios import (
    listar_livros, cadastrar_livro, atualizar_livro, deletar_livro,
    listar_clientes, cadastrar_cliente, atualizar_cliente, deletar_cliente
)

def menu_funcionario():
    opcoes = {
        "1": listar_livros,
        "2": cadastrar_livro,
        "3": atualizar_livro,
        "4": deletar_livro,
        "5": listar_clientes,
        "6": cadastrar_cliente,
        "7": atualizar_cliente,
        "8": deletar_cliente,
        "0": lambda: print("Saindo do menu funcionário...")
    }

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("=== SISTEMA DA BIBLIOTECA - FUNCIONÁRIO ===")
        print("1. Listar livros")
        print("2. Cadastrar livro")
        print("3. Atualizar livro")
        print("4. Deletar livro")
        print("5. Listar clientes")
        print("6. Cadastrar cliente")
        print("7. Atualizar cliente")
        print("8. Deletar cliente")
        print("0. Sair")

        opcao = input("Escolha uma opção: ")

        acao = opcoes.get(opcao)
        if acao:
            if opcao == "0":
                break
            acao()
        else:
            input("Opção inválida. Pressione Enter para continuar.")
