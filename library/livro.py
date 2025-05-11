from peewee import CharField, IntegerField, BooleanField
from library.config import ModeloBase

class Livro(ModeloBase):
    isbn = CharField(primary_key=True)
    titulo = CharField()
    autor = CharField()
    editora = CharField()
    ano_publicacao = IntegerField()
    genero = CharField()
    disponivel = BooleanField(default=True)

    def __str__(self):
        return f"{self.titulo} ({self.isbn})"
