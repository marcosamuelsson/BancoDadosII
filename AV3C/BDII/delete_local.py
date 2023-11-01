from config_local import *
from modelo_local import *

#deletando 
with app.app_context():
    p1 = Pessoa(pessoa_id = "1", nome= "João da Silva", email = "josilva@gmail.com")
    db.session.delete(p1)
    db.session.commit()
    print("Deu certo")