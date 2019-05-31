import json

from flask import Flask, render_template, jsonify
from flask_cors import CORS
from random import *
import requests

#models
from backend.models.overview import Overview
from backend.models.documentation import Document


#conn = psycopg2.connect("dbname=omnidbwebsite user=postgres")


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
CORS(
    app,
    origins="http://localhost:8080",
    allow_headers=[
        "Content-Type",
        "Access-Control-Allow-Origin",
        "Access-Control-Allow-Headers",
        "Access-Control-Allow-Methods",
        "Access-Control-Allow-Credentials"
    ],
    supports_credentials=True
)






@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    if app.debug:
        return requests.get('http://localhost:8080/{}'.format(path)).text

    pageTitle = 'OmniDB'
    pageSubtitle = 'Open Source Collaborative Environment For Database Management'


    context = {
        'data': {
            'pageTitle' : pageTitle,
            'pageSubtitle' : pageSubtitle
        }
    }
    return render_template("templates/index.html", context)






#Data routes
@app.route('/api/getOverview')
#@cross_origin(supports_credentials=True)
def overview():

    sections = Overview.getAll()

    context = {
        'data': sections
    }

    response = context

    return jsonify(response)


@app.route('/api/getDocumentation')
#@cross_origin(supports_credentials=True)
def documentation():

    documents = Document.getAll()

    context = {
        'data': documents
    }

    response = context

    return jsonify(response)
