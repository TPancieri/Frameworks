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
    data_prevista_devolucao: data prevista para devolução do livro
    data_devolucao: data da devolução do livro
    status: status atual do emprestimo ("emprestado" ou "devolvido")
    """
    id = AutoField() 
    livro = ForeignKeyField(Livro, backref='emprestimos', on_delete='CASCADE')
    usuario = ForeignKeyField(Usuario, backref='emprestimos', on_delete='CASCADE')
    data_emprestimo = DateTimeField(constraints=[SQL('DEFAULT CURRENT_TIMESTAMP')])
    data_prevista_devolucao = DateTimeField(null=False)
    data_devolucao = DateTimeField(null=True)
    status = CharField(choices=[
        ('emprestado', 'Emprestado'),
        ('devolvido', 'Devolvido')
    ], default='emprestado')

    def __str__(self):
        status_str = self.status
        if self.status == 'emprestado' and self.data_prevista_devolucao:
            status_str += f" (Devolver até: {self.data_prevista_devolucao.strftime('%d/%m/%Y')})"
        return f"Empréstimo {self.id}: {self.livro.titulo} para {self.usuario.nome} [{status_str}]"

    def esta_atrasado(self):
        """Verifica se o empréstimo está atrasado"""
        from datetime import datetime
        if self.status == 'emprestado' and datetime.now() > self.data_prevista_devolucao:
            return True
        return False
