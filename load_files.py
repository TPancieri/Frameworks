"""
Script para carregar dados iniciais no banco de dados.
Deve ser executado após create.py para popular o banco com dados de exemplo.
"""
from library import *
from datetime import datetime, timedelta

def carregar_dados():
    print("Iniciando carregamento dos dados...")
    db.connect()
    
    try:
        
        print("\nCarregando livros...")
        livros = [
            {"isbn": "9788595084759", "titulo": "O Senhor dos Anéis", "autor": "J.R.R. Tolkien", "editora": "HarperCollins", "ano_publicacao": 1954, "genero": "Fantasia"},
            {"isbn": "9788535914849", "titulo": "1984", "autor": "George Orwell", "editora": "Companhia das Letras", "ano_publicacao": 1949, "genero": "Distopia"},
            {"isbn": "9786554700016", "titulo": "Dom Casmurro", "autor": "Machado de Assis", "editora": "Editora Itatiaia", "ano_publicacao": 1899, "genero": "Romance"},
            {"isbn": "9788599296578", "titulo": "O Guia do Mochileiro das Galáxias", "autor": "Douglas Adams", "editora": "Sextante", "ano_publicacao": 1979, "genero": "Ficção Científica"}
        ]
        for l in livros:
            Livro.get_or_create(isbn=l["isbn"], defaults=l)
        print(f"{len(livros)} livros carregados.")

        
        print("\nCarregando funcionários...")
        funcionarios = [
            {"nome": "Ana Silva", "cpf": "12345678900", "email": "ana@biblioteca.com", "telefone": "99999-0001", "tipo": "funcionario"},
            {"nome": "Carlos Souza", "cpf": "98765432100", "email": "carlos@biblioteca.com", "telefone": "99999-0002", "tipo": "funcionario"}
        ]
        for f in funcionarios:
            Funcionario.get_or_create(cpf=f["cpf"], defaults=f)
        print(f"{len(funcionarios)} funcionários carregados.")

        
        print("\nCarregando clientes...")
        clientes = [
            {"nome": "Marcos Lima", "cpf": "11122233344", "email": "marcos@email.com", "telefone": "98888-0001", "tipo": "cliente"},
            {"nome": "Julia Alves", "cpf": "55566677788", "email": "julia@email.com", "telefone": "98888-0002", "tipo": "cliente"},
            {"nome": "Roberta Costa", "cpf": "99900011122", "email": "roberta@email.com", "telefone": "98888-0003", "tipo": "cliente"}
        ]
        cliente_objs = []
        for c in clientes:
            usuario = Usuario.get_or_create(cpf=c["cpf"], defaults=c)[0]
            cliente = Cliente.get_or_create(id=usuario.id, defaults=c)[0]
            cliente_objs.append(cliente)
        print(f"{len(clientes)} clientes carregados.")

        
        print("\nCriando empréstimos...")
        
        data_base = datetime.now() - timedelta(days=15)
        
        emprestimos = [
            # Empréstimo normal 
            {"isbn": "9788595084759", "cliente": cliente_objs[0], "data_emprestimo": data_base, "dias_emprestimo": 30},
            # Empréstimo atrasado 
            {"isbn": "9788535914849", "cliente": cliente_objs[1], "data_emprestimo": data_base, "dias_emprestimo": 10},
            # Empréstimo atrasado 
            {"isbn": "9786554700016", "cliente": cliente_objs[2], "data_emprestimo": data_base, "dias_emprestimo": 13}
        ]
        
        for e in emprestimos:
            try:
                livro = Livro.get_by_id(e["isbn"])
                
                data_prevista = e["data_emprestimo"] + timedelta(days=e["dias_emprestimo"])
                
                emprestimo_existente = (Emprestimo
                                     .select()
                                     .where(
                                         (Emprestimo.livro == livro) & 
                                         (Emprestimo.status == 'emprestado')
                                     )
                                     .first())
                
                if not emprestimo_existente:
                    Emprestimo.create(
                        livro=livro,
                        usuario_id=e["cliente"].id,
                        data_emprestimo=e["data_emprestimo"],
                        data_prevista_devolucao=data_prevista,
                        status='emprestado'
                    )
                    livro.disponivel = False
                    livro.save()
                    status = "ATRASADO" if data_prevista < datetime.now() else "No prazo"
                    print(f"Empréstimo criado: {livro.titulo} para {e['cliente'].nome} - Status: {status}")
                else:
                    print(f"Livro {livro.titulo} já está emprestado, pulando...")
                    
            except Exception as ex:
                print(f"Erro ao criar empréstimo para {e['isbn']}: {str(ex)}")
        
        print("\nCarregamento de dados concluído com sucesso!")
        
    except Exception as e:
        print(f"\nErro durante o carregamento: {str(e)}")
        db.rollback()
        raise
    finally:
        db.close()

if __name__ == '__main__':
    carregar_dados()
