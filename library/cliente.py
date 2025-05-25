"""
Modulo do cliente
"""

from .usuario import Usuario
from peewee import *

class Cliente(Usuario):
    """
    Modelo de dados para clientes da biblioteca.
    Herda de Usuario para compartilhar atributos básicos.
    """
    class Meta:
        table_name = 'cliente'
