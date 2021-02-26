# -*- coding: utf-8 -*-
#import os
#import cx_Oracle
from flask import Flask, jsonify, request
#import json
from utility_py.BaseController import BaseController
from utility_py.Tracing import LoggerAspect
from utility_py.CatchError import CatchError
from service.Configuration import Configuration
from service.OtorgantesService import OtorgantesService
from service.OracleDB import OracleDB

app = Flask(__name__)

@app.before_first_request
def load_configuration():
    global db
    global config
    config = Configuration().get_configuration()
    """db_user = os.getenv("DBAAS_USER_NAME")
    db_password = os.getenv("DBAAS_PASSWORD")
    db_server = os.getenv("DBAAS_SERVER")
    db_port = os.getenv("DBAAS_PORT")
    db_sid = os.getenv("DBAAS_SID")  """  
    db = OracleDB('cdc', 'c3Des#_R7i', '10.77.50.90', '1521', 'DESACC')
    #db = OracleDB(db_user, db_password, db_server, db_port, db_sid)



# Testing Route
@app.route('/', endpoint="start", methods=['GET'])
@CatchError()
@LoggerAspect
def test():
    return jsonify({'response': 'Start!'})

@app.route("/v1/obtener/otorgantes", endpoint="obt-otorgantes", methods=['GET'])
@CatchError()
@LoggerAspect
def ObtieneOtorgantes():
    obtoto = OtorgantesService().do_obtoto()
    return BaseController().success(obtoto, 'Petición exitosa', 'Se obtuvieron otorgantes', 200)



@app.route("/v1/conect/oracle", endpoint="conected-oracle", methods=['GET'])
@CatchError()
@LoggerAspect
def TestOracle():
    db.connect()
    db.cursor.execute("SELECT 'BD conectada!' FROM DUAL")
    result = db.cursor.fetchone()[0]
    #result = [x[0] for x in db.cursor]
    db.close()
    return BaseController().success(result, 'Petición exitosa', 'Se conecto de forma correcta', 200)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='8090')