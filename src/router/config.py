import os

ENV = os.getenv('ENV')
PORT = os.getenv('PORT', 5000)
DEBUG = ENV == 'development'
SECRET_KEY = os.getenv('SESSION_SECRET')
SESSION_TYPE = os.getenv('SESSION_TYPE')
