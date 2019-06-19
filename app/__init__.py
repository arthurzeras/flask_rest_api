# -*- coding: utf-8 -*-

from flask import Flask
from config import config
from .api import configure_api
from .db import db

def createApp(configName):
  app = Flask('api-users')

  app.config.from_object(config[configName])
  
  db.init_app(app)
  
  configure_api(app)

  return app