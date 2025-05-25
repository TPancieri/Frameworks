"""
Menu em loop, permite fazer o CRUD dos clientes e livros e organizar os emprestimos
"""
import os
from crud_funcionarios import (
    listar_livros, cadastrar_livro, atualizar_livro, deletar_livro,
    listar_clientes, cadastrar_cliente, atualizar_cliente, deletar_cliente, 
    emprestar_livro, devolver_livro
)
from crud_livros import buscar_livros
from crud_clientes import listar_emprestimos_ativos, listar_clientes_atrasados

def menu_livros():
    opcoes = {
        "1": listar_livros,
        "2": buscar_livros,
        "3": cadastrar_livro,
        "4": atualizar_livro,
        "5": deletar_livro,
        "0": lambda: None
    }

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("=== OPERAÇÕES DE LIVROS ===")
        print("1. Listar livros")
        print("2. Buscar livros")
        print("3. Cadastrar livro")
        print("4. Atualizar livro")
        print("5. Deletar livro")
        print("0. Voltar ao menu principal")

        opcao = input("\nEscolha uma opção: ")

        acao = opcoes.get(opcao)
        if acao:
            if opcao == "0":
                break
            acao()
        else:
            input("Opção inválida. Pressione Enter para continuar.")

def menu_clientes():
    opcoes = {
        "1": listar_clientes,
        "2": listar_emprestimos_ativos,
        "3": listar_clientes_atrasados,
        "4": cadastrar_cliente,
        "5": atualizar_cliente,
        "6": deletar_cliente,
        "7": emprestar_livro,
        "8": devolver_livro,
        "0": lambda: None
    }

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("=== OPERAÇÕES DE CLIENTES ===")
        print("1. Listar clientes")
        print("2. Listar empréstimos ativos")
        print("3. Listar clientes com atrasos")
        print("4. Cadastrar cliente")
        print("5. Atualizar cliente")
        print("6. Deletar cliente")
        print("7. Emprestar livro")
        print("8. Devolver livro")
        print("0. Voltar ao menu principal")

        opcao = input("\nEscolha uma opção: ")

        acao = opcoes.get(opcao)
        if acao:
            if opcao == "0":
                break
            acao()
        else:
            input("Opção inválida. Pressione Enter para continuar.")

def menu_funcionario():
    opcoes = {
        "1": menu_livros,
        "2": menu_clientes,
        "0": lambda: print("Saindo do sistema...")
    }

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("=== SISTEMA DA BIBLIOTECA ===")
        print("1. Operações de Livros")
        print("2. Operações de Clientes")
        print("0. Sair")

        opcao = input("\nEscolha uma opção: ")

        acao = opcoes.get(opcao)
        if acao:
            if opcao == "0":
                break
            acao()
        else:
            input("Opção inválida. Pressione Enter para continuar.")
