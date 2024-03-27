from flask import Flask
app = Flask(__name__)

import psycopg2

@app.route('/db_test')
def test():
    conn = psycopg2.connect("postgres://alex_goose_user:YAkvAHGowhcdbAyYsGIuFHWHxVf51FIF@dpg-co24jo0l5elc73d47vt0-a/alex_goose")
    conn.close()
    return "Database connection successful!"

@app.route('/')
def hello_world():
    return 'Hello World from Alexander Gustafson is 3308!'


