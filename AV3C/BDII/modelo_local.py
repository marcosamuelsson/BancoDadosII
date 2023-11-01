import config_local as cl

class Pessoa(cl.db.Model):
    __tablename__ = 'hylson_sqlalchemy_pessoa'
    # atributos da pessoa
    pessoa_id = cl.db.Column('pessoa_id', cl.db.Integer, primary_key=True)
    nome = cl.db.Column(cl.db.String(254))
    email = cl.db.Column(cl.db.String(254))
    
    # método para expressar a pessoa em forma de texto
    def __str__(self):
        return f'''{self.pessoa_id},
        {self.nome}
        {self.email}
        '''
