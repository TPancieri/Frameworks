"""
Menu em loop, permite fazer o CRUD dos clientes e livros e organizar os emprestimos
"""
import os
from crud_funcionarios import (
    listar_livros, cadastrar_livro, atualizar_livro, deletar_livro,
    listar_clientes, cadastrar_cliente, atualizar_cliente, deletar_cliente, 
    emprestar_livro, devolver_livro
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
        "9": emprestar_livro,
        "10": devolver_livro,
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
        print("9. Emprestar livro")
        print("10. Devolver livro")
        print("0. Sair")

        opcao = input("Escolha uma opção: ")

        acao = opcoes.get(opcao)
        if acao:
            if opcao == "0":
                break
            acao()
        else:
            input("Opção inválida. Pressione Enter para continuar.")
