import config_local as cl
import modelo_local as ml
import config_remoto as cr
import modelo_remoto as mr

'''
with cl.app.app_context():

    # criar pessoa localmente
    p1 = ml.Pessoa(nome = "João da Silva", 
        email = "josilva@gmail.com")
    cl.db.session.add(p1)
    cl.db.session.commit()

    print(f"Pessoa criada: {p1}")
'''
meu_celular = None
minha_pessoa = None
pessoa_id_temp = 0

with cr.app.app_context():

    # criar celular remotamente
    meu_celular = mr.Celular(pessoa_id = 1, marca = "Samsung", 
                modelo = "S5", numero = '47 9 9292-1234')
    cr.db.session.add(meu_celular)
    cr.db.session.commit()

    print("Celular criado") 

    # associação temporária
    pessoa_id_temp = meu_celular.pessoa_id
    
# buscar a pessoa
with cl.app.app_context():
    minha_pessoa = cl.db.session.get(ml.Pessoa, pessoa_id_temp)
    print("Pessoa encontrada no local")

# associando
meu_celular.pessoa = minha_pessoa

# mostrando o atributo composto
print(meu_celular.pessoa.nome)