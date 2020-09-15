from flask import Flask
from config import DevConfig
# from flask_bootstrap import Bootstrap

#initializing app

app = Flask(__name__,instance_relative_config = True)

#config
app.config.from_object(DevConfig)
app.config.from_pyfile('config.py')


from app import views