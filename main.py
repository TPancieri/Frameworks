from library.config import db
from menu import menu_funcionario

if __name__ == "__main__":
    db.connect()
    menu_funcionario()
    db.close()
