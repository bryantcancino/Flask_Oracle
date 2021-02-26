# -*- coding: utf-8 -*-
from service.OracleDB import OracleDB
import os
import cx_Oracle
from utility_py.BaseValidator import BaseValidator
from utility_py.InternalException import InternalException

class OtorgantesService:
    
    def __init__(self):
        db_user = os.getenv("DBAAS_USER_NAME")
        db_password = os.getenv("DBAAS_PASSWORD")
        db_server = os.getenv("DBAAS_SERVER")
        db_port = os.getenv("DBAAS_PORT")
        db_sid = os.getenv("DBAAS_SID")
        self.db = OracleDB(db_user, db_password, db_server, db_port, db_sid)

    def do_obtoto(self):
        try:
            self.db.connect()
            PCUR_OTORGANTE = self.db.cursor.var(cx_Oracle.CURSOR)
            PMENSAJE_ERROR = self.db.cursor.var(cx_Oracle.STRING)
            l_query = self.db.cursor.callproc("CCSP_OBTIENE_OTORGANTE", [PCUR_OTORGANTE, PMENSAJE_ERROR])
            l_results = l_query[0]
            response = []
            #lst = list(l_results)
            #print(len(lst))
            for cell in l_results:
                newNode = {
                        'NUMERO_OTORGANTE':cell[0],
                        'RAZON_SOCIAL':cell[1]
                }
                #response.append({cell[0] : newNode})
                response.append(newNode)
            if response is None:
                errors = InternalException()
                errors.add(BaseValidator.get_business_error(
                    "E001",
                    "Error",
                    "Error al extraer datos. No se encontraron otorgantes",
                    status_code = 404)
                )
                errors.launch()        
        
        except cx_Oracle.DatabaseError as e:
            print("Problema al conectarse con Oracle", e)
        finally:
            self.db.close()            

        return response
