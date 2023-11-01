import config_remoto as cr
import config_local as cl
from modelo_local import Pessoa

class Celular(cr.db.Model):
    __tablename__ = 'hylson_sqlalchemy_celular'
    # atributos da pessoa
    celular_id = cr.db.Column('celular_id', cr.db.Integer, primary_key=True)
    
    pessoa_id = cr.db.Column(cr.db.Integer)
    
    marca = cr.db.Column(cr.db.String(254))
    modelo = cr.db.Column(cr.db.String(254))
    numero = cr.db.Column(cr.db.String(254))