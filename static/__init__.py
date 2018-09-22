from flask import Flask
from static.config import Config

app = Flask(__name__)
app.config.from_object(Config)

from static import routes
