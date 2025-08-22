from flask import Flask
import tomllib

app = Flask(__name__)
app.config.from_file("../config.toml", load=tomllib.load, text=False)
app.config.from_file("/etc/MATERIAL_CONFIG/credentials.toml", load=tomllib.load, text=False)
from app import routes
