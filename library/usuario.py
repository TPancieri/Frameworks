from .config import ModeloBase
from peewee import *

class Usuario(ModeloBase):
    id = AutoField()  
    nome = CharField(null=False)
    cpf = CharField(unique=True, null=False)
    email = CharField(unique=True, null=False)
    telefone = CharField(null=False)
    data_cadastro = DateTimeField(constraints=[SQL('DEFAULT CURRENT_TIMESTAMP')], null=False)
    tipo = CharField(null=False)

    class Meta:
        table_name = 'usuario'
        indexes = (
            (('cpf',), True),
            (('email',), True),
        )
