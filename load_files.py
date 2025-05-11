from library import *

db.connect()

livros = [
    {"isbn": "9788595084759", "titulo": "O Senhor dos Anéis", "autor": "J.R.R. Tolkien", "editora": "HarperCollins", "ano_publicacao": 1954, "genero": "Fantasia"},
    {"isbn": "9788535914849", "titulo": "1984", "autor": "George Orwell", "editora": "Companhia das Letras", "ano_publicacao": 1949, "genero": "Distopia"},
    {"isbn": "9786554700016", "titulo": "Dom Casmurro", "autor": "Machado de Assis", "editora": "Editora Itatiaia", "ano_publicacao": 1899, "genero": "Romance"},
    {"isbn": "9788599296578", "titulo": "O Guia do Mochileiro das Galáxias", "autor": "Douglas Adams", "editora": "Sextante", "ano_publicacao": 1979, "genero": "Ficção Científica"}
]
for l in livros:
    Livro.get_or_create(isbn=l["isbn"], defaults=l)

funcionarios = [
    {"nome": "Ana Silva", "cpf": "12345678900", "email": "ana@biblioteca.com", "telefone": "99999-0001", "tipo": "funcionario"},
    {"nome": "Carlos Souza", "cpf": "98765432100", "email": "carlos@biblioteca.com", "telefone": "99999-0002", "tipo": "funcionario"}
]
for f in funcionarios:
    Funcionario.get_or_create(cpf=f["cpf"], defaults=f)

clientes = [
    {"nome": "Marcos Lima", "cpf": "11122233344", "email": "marcos@email.com", "telefone": "98888-0001", "tipo": "cliente"},
    {"nome": "Julia Alves", "cpf": "55566677788", "email": "julia@email.com", "telefone": "98888-0002", "tipo": "cliente"},
    {"nome": "Roberta Costa", "cpf": "99900011122", "email": "roberta@email.com", "telefone": "98888-0003", "tipo": "cliente"}
]
cliente_objs = []
for c in clientes:
    obj, created = Cliente.get_or_create(cpf=c["cpf"], defaults=c)
    cliente_objs.append(obj)

emprestimos = [
    {"isbn": "9788595084759", "cliente": cliente_objs[0]},
    {"isbn": "9788535914849", "cliente": cliente_objs[1]},
    {"isbn": "9786554700016", "cliente": cliente_objs[2]},
]
for e in emprestimos:
    livro = Livro.get_by_id(e["isbn"])
    e["cliente"].pedir_livro(livro)

db.close()
