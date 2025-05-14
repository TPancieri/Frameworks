"""
Exporta os modelos e conexão do db para acesso mais fácil
"""

from .config import db
from .livro import Livro
from .usuario import Usuario
from .cliente import Cliente
from .funcionario import Funcionario
from .emprestimo import Emprestimo

# Define o que é exportado quando usa "from library import *", deixa mais facil de importar
__all__ = ["db", "Livro", "Usuario", "Cliente", "Funcionario", "Emprestimo"]
