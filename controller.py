from flask import Flask, request, jsonify, make_response
from model import Model


app = Flask(__name__)

@app.route('/v1/ac04/consultar/', methods=["GET"])
def consultar():
    return Model.jsonReturn()


@app.route('/v1/ac04/consultar/cliente', methods=["GET"])
def consultarCliente():
    return Model.soma()

if __name__ == '__main__':
    app.run(debug=True,port= 5000)