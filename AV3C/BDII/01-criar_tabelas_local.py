from config_local import *
from modelo_local import *

# criando contexto para a aplicação :-/
with app.app_context():

    # criar tabelas
    db.create_all()

    print("Tabelas criadas")