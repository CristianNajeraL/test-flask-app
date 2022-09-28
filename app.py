import os
from flask import Flask
import pandas as pd
from sqlalchemy import create_engine


DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_PORT = os.getenv("DB_PORT")
DB_USERNAME = os.getenv("DB_USERNAME")

print(f'postgresql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}')

app = Flask(__name__)


@app.route('/')
def hello_world():
    return f'After pipeline'


if __name__ == '__main__':
    app.run()
