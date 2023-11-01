# importações
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

# flask
app = Flask(__name__)

# OPÇÃO 2: sqlalchemy com mysql ------------------
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:root@localhost/Marco"

# configurações comuns para opção 1 e 2
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)