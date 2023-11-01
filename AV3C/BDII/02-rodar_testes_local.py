from config_local import *
from modelo_local import *

# criando contexto para a aplicação :-/
with app.app_context():

    # criar pessoas
    p1 = Pessoa(nome = "João da Silva", 
        email = "josilva@gmail.com")
    db.session.add(p1)
    db.session.commit()

    print(f"Pessoa criada: {p1}")
