from peewee import AutoField, CharField, DateTimeField, ForeignKeyField, SQL
from library.config import ModeloBase
from library.livro import Livro
from library.usuario import Usuario

class Emprestimo(ModeloBase):
    """
    id: chave primaria com Auto increment
    livro: referencia para o livro emprestado
    usuario: referencia para o usuario pegando o livro
    data_emprestimo: data do emprestimo do livro
    data_devolucao: data da devolução do livro
    status: status atual do emprestimo ("emprestado" ou "devolvido")
    """
    id = AutoField() 
    livro = ForeignKeyField(Livro, backref='emprestimos', on_delete='CASCADE')
    usuario = ForeignKeyField(Usuario, backref='emprestimos', on_delete='CASCADE')
    data_emprestimo = DateTimeField(constraints=[SQL('DEFAULT CURRENT_TIMESTAMP')])
    data_devolucao = DateTimeField(null=True)
    status = CharField(choices=[
        ('emprestado', 'Emprestado'),
        ('devolvido', 'Devolvido')
    ], default='emprestado')

    def __str__(self):
        return f"Empréstimo {self.id}: {self.livro.titulo} para {self.usuario.nome} [{self.status}]"
