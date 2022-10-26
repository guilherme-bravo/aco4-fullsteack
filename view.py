from flask import Flask, request, jsonify, make_response
import json

app = Flask(__name__)

tasks = [
    {
        'id': 1,
        'name': "task1",
        "description": "This is task 1"
    },
    {
        "id": 2,
        "name": "task2",
        "description": "This is task 2"
    },
    {
        "id": 3,
        "name": "task3",
        "description": "This is task 3"
    }
]

tasksJSON = json.dumps(tasks)


@app.route('/v1/ac04/cadastrar', methods=["POST"])
def cadastrar():
     input_json = request.get_json(force=True) 
     jsonToReturn = {'nome':input_json['nome'], 'Cadastro':'Efetuado com sucesso'}
     return jsonify(jsonToReturn), 200


@app.route('/v1/ac04/consultar/', methods=["GET"])
def consultar():
    jsonToReturn = {'id':'1', 'name':'Mariana'}, {'id':'2', 'name':'Guilherme'}
    return jsonToReturn





