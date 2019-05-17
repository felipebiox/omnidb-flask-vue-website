import psycopg2
import json

from flask import Flask, render_template, jsonify
from flask_cors import CORS
from random import *
import requests


conn = psycopg2.connect("dbname=omnidbwebsite user=postgres")


class CustomFlask(Flask):
    jinja_options = Flask.jinja_options.copy()
    jinja_options.update(dict(
      block_start_string='{%',
      block_end_string='%}',
      variable_start_string='((',
      variable_end_string='))',
      comment_start_string='{#',
      comment_end_string='#}',
    ))




app = CustomFlask(__name__,
            static_url_path = '/static',
            static_folder = "./dist/static",
            template_folder = "./dist")
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})






@app.route('/api/random')
def random_number():
    response = {
        'randomNumber': randint(1, 100)
    }
    return jsonify(response)



@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    if app.debug:
        return requests.get('http://localhost:8080/{}'.format(path)).text
    return render_template("templates/index.html")






#Data routes
@app.route('/api/getDocumentation')
def documentation():

    cur = conn.cursor()

    cur.execute("SELECT * FROM public.documentation;")

    result = cur.fetchall()

    items = [];

    for item in result:
        items.append(
            {
                'title' : item[0],
                'alias' : item[1],
                'introtext' : item[2],
                'modified'  : item[3]
            }
        )

    data = items

    context = {
        'data': data
    }

    response = context

    return jsonify(response)
