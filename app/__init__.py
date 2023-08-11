from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

from app import routes

# Configuração para lidar com caracteres especiais
app.config['JSON_AS_ASCII'] = False
