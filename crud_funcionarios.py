from library import *
from library.livro import Livro
from library.cliente import Cliente
from library.funcionario import Funcionario

from crud_livros import (
    listar_livros,
    cadastrar_livro,
    atualizar_livro,
    deletar_livro,
    buscar_livro_por_titulo_ou_isbn
)

from crud_clientes import (
    listar_clientes,
    cadastrar_cliente,
    atualizar_cliente,
    deletar_cliente,
    buscar_cliente_por_nome_ou_email
)

from crud_emprestimos import (
    emprestar_livro,
    devolver_livro
)
