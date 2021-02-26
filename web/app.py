# -*- coding: utf-8 -*-
import os
#import cx_Oracle
from flask import Flask, jsonify, request
#import json
import logging
from utility_py.BaseController import BaseController
from utility_py.Tracing import LoggerAspect
from utility_py.CatchError import CatchError
from service.Configuration import Configuration
from service.OtorgantesService import OtorgantesService
from service.OracleDB import OracleDB

app = Flask(__name__)

@app.before_first_request
def load_configuration():
    app.logger.info("Before First Request")
    #global db
    #global config

# Testing Route
@app.route('/', endpoint="start", methods=['GET'])
@CatchError()
@LoggerAspect
def test():
    return jsonify({'response': 'Start!'})

@app.route("/v1/obtener/data", endpoint="obt-data", methods=['GET'])
@CatchError()
@LoggerAspect
def ObtieneOtorgantes():
    obtoto = OtorgantesService().sp_obtoto()
    return BaseController().success(obtoto, 'Petición exitosa', 'Se obtuvieron data', 200)


@app.route("/v1/conect/oracle", endpoint="conected-oracle", methods=['GET'])
@CatchError()
@LoggerAspect
def TestOracle():
    db_user = os.getenv("DBAAS_USER_NAME")
    db_password = os.getenv("DBAAS_PASSWORD")
    db_server = os.getenv("DBAAS_SERVER")
    db_port = os.getenv("DBAAS_PORT")
    db_sid = os.getenv("DBAAS_SID")    
    db = OracleDB(db_user, db_password, db_server, db_port, db_sid)
    db.connect()
    db.cursor.execute("SELECT 'BD conectada!' FROM DUAL")
    result = db.cursor.fetchone()[0]
    #result = [x[0] for x in db.cursor]
    db.close()
    return BaseController().success(result, 'Petición exitosa', 'Se conecto de forma correcta', 200)


if __name__ == '__main__':
    Configuration().get_configuration() 
    app.run(debug=True, host='0.0.0.0', port=os.getenv("SERVER_PORT"))