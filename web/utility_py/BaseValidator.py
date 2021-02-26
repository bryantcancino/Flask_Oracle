# -*- coding: utf-8 -*-
import re
from utility_py.GenericResponse import InternalError
from http import HTTPStatus

class BaseValidator:
    TYPE_STRINGS = [str]

    def __init__(self):
        pass

    @staticmethod
    def get_dict(key, field=None, error=None):
        return {'key': key, 'field': field, 'error': error}

    """ 
        Valida el tipo de dato segun sea el caso
        @param field, nombre del campo
        @param value, dato a validar
        @param type_of, tipo de dato deseado
    """
    @staticmethod
    def valida_tipo_dato(field, value, type_of):
        if type_of is 'string':
            if not type(value) in BaseValidator.TYPE_STRINGS:
                return BaseValidator.get_dict('VALIDACION_TIPO_STRING', field=field)
            else:
                return None
        elif type_of is 'int':
            if not type(value) is int:
                return BaseValidator.get_dict('VALIDACION_TIPO_INT', field=field)
            else:
                return None
        elif type_of is 'float':
            if not type(value) is float:
                return BaseValidator.get_dict('VALIDACION_TIPO_FLOAT', field=field)
            else:
                return None
        elif type_of is 'list':
            if not type(value) is list:
                return BaseValidator.get_dict('VALIDACION_TIPO_LISTA', field=field)
            else:
                return None
        elif type_of is 'object':
            if not type(value) is dict:
                return BaseValidator.get_dict('VALIDACION_TIPO_OBJETO', field=field)
            else:
                return None
        return None

    """ 
        Valida que el dato este vacio
        @param field, nombre del campo
        @param value, dato a validar
    """
    @staticmethod
    def valida_no_nulo(field, value):
        if value is None:
            return BaseValidator.get_dict('VALIDACION_CAMPO_NULO', field=field)
        return None

    """ 
        Valida que el dato este vacio
        @param field, nombre del campo
        @param value, dato a validar
    """
    @staticmethod
    def valida_requerido(field, value):
        if len(value.strip()) is 0:
            return BaseValidator.get_dict('VALIDACION_CAMPO_VACIO', field=field)
        return None

    """ 
        Valida que el dato cumpla con el formato de la expresión regular
        @param field, nombre del campo
        @param value, dato a validar
        @param regex, expresión regular con la que debe coincidir
    """
    @staticmethod
    def valida_formato(field, value, regex):
        if not re.match(regex, value):
            return BaseValidator.get_dict('VALIDACION_FORMATO', field=field)
        return None

    """ 
        Sustituye el error llamado NEGOCIO, con los datos entrantes.
        @param code, código de error interno.
        @param title, título del error; ejemplo "Error" o "Alerta".
        @param message, descripción breve de lo ocurrido.
        @param detail, puede contener la descripción completa del problema.
        @param status_code, es el número del enum del estándar de status codes.
    """
    @staticmethod
    def get_business_error(code, title, message, detail=None, status_code=None):
        if code is None or title is None or message is None:
            raise Exception('code, title and message are mandatory')
        if status_code is not None:
            status_code_object = HTTPStatus(int(status_code))
        else:
            status_code_object = None
        error = InternalError(code, title, message, detail=detail, status_code_object=status_code_object)

        return BaseValidator.get_dict('NEGOCIO', error=error)
