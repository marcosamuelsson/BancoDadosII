# importações
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

# flask
app = Flask(__name__)

#app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://hylsonco_bd2_2023_ifc:chalala1990@62.77.153.140/hylsonco_bd2_2023_ifc"

# sqlalchemy com sqlite
path = os.path.dirname(os.path.abspath(__file__)) 
arquivobd = os.path.join(path, 'bd_local_sqlite.db')
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///"+arquivobd


# configurações comuns para opção 1 e 2
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

