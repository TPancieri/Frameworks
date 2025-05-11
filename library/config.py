from peewee import Model, SqliteDatabase

db = SqliteDatabase('biblioteca.db')

class ModeloBase(Model):
    class Meta:
        database = db
