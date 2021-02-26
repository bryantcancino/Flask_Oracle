# -*- coding: utf-8 -*-
import copy as c
from utility_py.GenericResponse import InternalError
from http import HTTPStatus

class Errors(object):

    def __init__(self):
        self.errors = {
            "GENERAL_GENERICO_PUBLICO":           InternalError("GE001", "InternalError", "Ocurrio un problema, intentelo nuevamente mas tarde.",          False, HTTPStatus.INTERNAL_SERVER_ERROR),
            "GENERAL_GENERICO":                   InternalError("GE002", "Error", "Error.",                                                                True,  HTTPStatus.INTERNAL_SERVER_ERROR),
            "GENERAL_NO_IMPLEMENTADO":            InternalError("GE003", "Error", "Servicio no implementado.",                                             True,  HTTPStatus.NOT_IMPLEMENTED),
            "GENERAL_NO_ENTORNO":                 InternalError("GE004", "Error", "No se definió un ambiente de ejecucion.",                               True,  HTTPStatus.INTERNAL_SERVER_ERROR),
            "GENERAL_PETICION_ERRONEA":           InternalError("GE005", "Error", "Error al procesar su petición",                                         True,  HTTPStatus.BAD_REQUEST),
            "GENERAL_FORMATO_OBJETO":             InternalError("GE006", "Error", "Error al serializar el objeto.",                                        True,  HTTPStatus.INTERNAL_SERVER_ERROR),
            "GENERAL_CREACION_ARCHIVO":           InternalError("GE007", "Error", "Error al crear crear el archivo \"{Archivo}\".",                        True,  HTTPStatus.INTERNAL_SERVER_ERROR),
            "GENERAL_PARAMETROS_VACIOS":          InternalError("GE008", "Error", "Ocurrio un problema, parámetro de solicitud faltante.",                 False, HTTPStatus.BAD_REQUEST),
            "GENERAL_FORMATO_JSON_ERRORNEO":      InternalError("GE009", "Error", "Ocurrio un problema, el formato del json no es correcto.",              False, HTTPStatus.BAD_REQUEST),
            "GENERAL_FORMATO_FECHA_ERRORNEO":     InternalError("GE010", "Error", "Ocurrio un problema, el formato de la fecha no es correcto.",           False, HTTPStatus.BAD_REQUEST),
            "GENERAL_FORMATO_OBJETO_ASINCRONO":   InternalError("GE011", "Error", "El formato del objeto es de tipo asincrono y no puede ser procesado.",  False, HTTPStatus.BAD_REQUEST),


            "CONECTIVIDAD_DB":                    InternalError("CO001", "Error", "Problemas de conectividad con la base de datos.",                       True,  HTTPStatus.SERVICE_UNAVAILABLE),
            "CONECTIVIDAD_WS":                    InternalError("CO002", "Error", "Problemas de conectividad con servicios externos.",                     True,  HTTPStatus.SERVICE_UNAVAILABLE),
            "CONECTIVIDAD_REST":                  InternalError("CO003", "Error", "Problemas de conectividad con el recurso externo.",                     True,  HTTPStatus.SERVICE_UNAVAILABLE),
            "CONECTIVIDAD_CORREO":                InternalError("CO004", "Error", "Problemas de conectividad con el servicio de correo.",                  True,  HTTPStatus.SERVICE_UNAVAILABLE),

            "BASEDATOS_CONSULTA_MALFORMDA":       InternalError("BD001", "Error", "Error, verifique la consulta.",                                         True,  HTTPStatus.INTERNAL_SERVER_ERROR),
            "BASEDATOS_DATOS_UNICOS":             InternalError("BD002", "Error", "Error de base de datos, no se cumple la unicidad de datos.",            True,  HTTPStatus.INTERNAL_SERVER_ERROR),
            "BASEDATOS_DATOS_RESTRICCION":        InternalError("BD003", "Error", "Error de base de datos, no se cumple la dependencia entre datos.",      True,  HTTPStatus.INTERNAL_SERVER_ERROR),
            "BASEDATOS_DATOS_CONCURRENCIA":       InternalError("BD004", "Error", "Error de base de datos, existe un candado en la tabla.",                True,  HTTPStatus.SERVICE_UNAVAILABLE),
            "BASEDATOS_DATOS_FORMATO":            InternalError("BD005", "Error", "Error, verifique la extraccion de los datos.",                          False, HTTPStatus.INTERNAL_SERVER_ERROR),
            "BASEDATOS_PERMISOS_RECURSO":         InternalError("BD006", "Error", "Error, no fue posible acceder al recurso.",                             False, HTTPStatus.INTERNAL_SERVER_ERROR),

            "SEGURIDAD_CREDENCIALES_ERROR":       InternalError("SE001", "Alerta", "Error, verifique sus credenciales.",                                    False, HTTPStatus.FORBIDDEN),
            "SEGURIDAD_TOKEN_ERROR":              InternalError("SE002", "Alerta", "Error, no fue posible autenticar el usuario.",                          False, HTTPStatus.FORBIDDEN),
            "SEGURIDAD_TOKEN_CADUCO":             InternalError("SE003", "Alerta", "Error, su sesion ha caducado.",                                         False, HTTPStatus.UNAUTHORIZED),
            "SEGURIDAD_PERMISOS_EXCEDEN_ROL":     InternalError("SE004", "Alerta", "Error, no cuenta con los permisos suficientes para acceder.",           False, HTTPStatus.UNAUTHORIZED),
            "SEGURIDAD_PERMISOS_RECURSO":         InternalError("SE005", "Alerta", "Error, no fue posible acceder al recurso.",                             False, HTTPStatus.UNAUTHORIZED),

            "VALIDACION_CAMPO_NULO":              InternalError("VA001", "Alerta", "El campo \"{Campo}\" no puede estar vacio.",                            False, HTTPStatus.BAD_REQUEST),
            "VALIDACION_CAMPO_VACIO":             InternalError("VA002", "Alerta", "El campo \"{Campo}\" no puede estar vacio.",                            False, HTTPStatus.BAD_REQUEST),
            "VALIDACION_CAMPO_REQUERIDO":         InternalError("VA003", "Alerta", "El campo \"{Campo}\" es requerido.",                                    False, HTTPStatus.BAD_REQUEST),
            "VALIDACION_LONGITUD_MINIMA":         InternalError("VA004", "Alerta", "El campo \"{Campo}\" no cumple con la longitud minima.",                False, HTTPStatus.BAD_REQUEST),
            "VALIDACION_LONGITUD_MAXIMA":         InternalError("VA005", "Alerta", "El campo \"{Campo}\" excede la longitud permitida.",                    False, HTTPStatus.BAD_REQUEST),
            "VALIDACION_LONGITUD_RANGO":          InternalError("VA006", "Alerta", "El campo \"{Campo}\" no cumple con la longitud permitida.",             False, HTTPStatus.BAD_REQUEST),
            "VALIDACION_FORMATO":                 InternalError("VA007", "Alerta", "El campo \"{Campo}\" no cumple con el formato permitido.",              False, HTTPStatus.BAD_REQUEST),
            "VALIDACION_DUPLICIDAD":              InternalError("VA008", "Alerta", "El campo \"{Campo}\" no cumple con el formato permitido.",              False, HTTPStatus.BAD_REQUEST),
            "VALIDACION_IDENTIDAD":               InternalError("VA009", "Alerta", "Los campos \"{Campo}\" no coinciden.",                                  False, HTTPStatus.BAD_REQUEST),
            "VALIDACION_NEGATIVO":                InternalError("VA010", "Alerta", "El campo \"{Campo}\" no puede ser menor a cero.",                       False, HTTPStatus.BAD_REQUEST),
            "VALIDACION_FECHA":                   InternalError("VA011", "Alerta", "El campo \"{Campo}\" no es una fecha valida.",                          False, HTTPStatus.BAD_REQUEST),
            "VALIDACION_BIRTHDATE":               InternalError("VA012", "Alerta", "El campo \"{Campo}\" no esta en el rango permitido",                    False, HTTPStatus.BAD_REQUEST),
            "VALIDACION_PAIS":                    InternalError("VA013", "Alerta", "El campo \"{Campo}\" no esta dentro del catalogo de paises.",           False, HTTPStatus.BAD_REQUEST),
            "VALIDACION_ESTADO":                  InternalError("VA014", "Alerta", "El campo \"{Campo}\" no esta dentro del catalogo de estados.",          False, HTTPStatus.BAD_REQUEST),
            "VALIDACION_MUNICIPIO":               InternalError("VA015", "Alerta", "El campo \"{Campo}\" no esta dentro del catalogo de municipios.",       False, HTTPStatus.BAD_REQUEST),
            "VALIDACION_NACIONALIDAD":            InternalError("VA016", "Alerta", "El campo \"{Campo}\" no esta dentro del catalogo de nacionalidades.",   False, HTTPStatus.BAD_REQUEST),
            "VALIDACION_RFC_FECHA":               InternalError("VA017", "Alerta", "El campo \"{Campo}\" no coincide con la fecha de nacimiento dada.",     False, HTTPStatus.BAD_REQUEST),
            "VALIDACION_CP_EN_ESTADO":            InternalError("VA018", "Alerta", "El campo \"{Campo}\" no se encuentra en el estado dado.",               False, HTTPStatus.BAD_REQUEST),
            "VALIDACION_TIPO_RESPONSABILIDAD":    InternalError("VA019", "Alerta", "El campo \"{Campo}\" no esta en el catalogo.",                          False, HTTPStatus.BAD_REQUEST),
            "VALIDACION_TIPO_CUENTA":             InternalError("VA020", "Alerta", "El campo \"{Campo}\" no esta dentro del catalogo tipo de cuenta.",      False, HTTPStatus.BAD_REQUEST),
            "VALIDACION_TIPO_CONTRATO":           InternalError("VA021", "Alerta", "El campo \"{Campo}\" no esta dentro del catalogo de tipo de contrato.", False, HTTPStatus.BAD_REQUEST),
            "VALIDACION_CVE_MONEDA":              InternalError("VA022", "Alerta", "El campo \"{Campo}\" no reconoce la clave de moneda dada.",             False, HTTPStatus.BAD_REQUEST),
            "VALIDACION_CVE_PREVENCION":          InternalError("VA023", "Alerta", "El campo \"{Campo}\" no reconoce la clave de prevencion dada.",         False, HTTPStatus.BAD_REQUEST),
            "VALIDACION_CAT_FRECUENCIA_PAGOS":    InternalError("VA024", "Alerta", "El campo \"{Campo}\" no reconoce la clave dada.",                       False, HTTPStatus.BAD_REQUEST),
            "VALIDACION_PAGO_ACTUAL":             InternalError("VA025", "Alerta", "El campo \"{Campo}\" no es valido.",                                    False, HTTPStatus.BAD_REQUEST),
            "VALIDACION_CURP":                    InternalError("VA026", "Alerta", "El campo \"{Campo}\" no cumple con la estructura permitida.",           False, HTTPStatus.BAD_REQUEST),
            "VALIDACION_RFC":                     InternalError("VA027", "Alerta", "El campo \"{Campo}\" no cumple con la estructura permitida.",           False, HTTPStatus.BAD_REQUEST),
            "VALIDACION_ALPHANUMERIC_ALPHA":      InternalError("VA028", "Alerta", "El campo \"{Campo}\" no cumple con la estructura permitida. Solo numeros y letras", False, HTTPStatus.BAD_REQUEST),
            "VALIDACION_TIPO_STRING":             InternalError("VA029", "Alerta", "El campo \"{Campo}\" debe ser un string.",                              False, HTTPStatus.BAD_REQUEST),
            "VALIDACION_TIPO_INT":                InternalError("VA030", "Alerta", "El campo \"{Campo}\" debe ser un int.",                                 False, HTTPStatus.BAD_REQUEST),
            "VALIDACION_TIPO_FLOAT":              InternalError("VA031", "Alerta", "El campo \"{Campo}\" debe ser un float.",                               False, HTTPStatus.BAD_REQUEST),
            "VALIDACION_TIPO_LISTA":              InternalError("VA032", "Alerta", "El campo \"{Campo}\" debe ser una lista[].",                            False, HTTPStatus.BAD_REQUEST),
            "VALIDACION_TIPO_OBJETO":             InternalError("VA033", "Alerta", "El campo \"{Campo}\" debe ser un objeto{}.",                            False, HTTPStatus.BAD_REQUEST),
            "GRAPHQL_ERROR_GENERICO":             InternalError("GR001", "Alerta", "Error, la consulta graphql no puede ser procesada.",                    False, HTTPStatus.BAD_REQUEST),
            "NEGOCIO":                            InternalError("BU000", "Alerta", "Error, agregar algun error de negocio.",                                False, HTTPStatus.ACCEPTED),
            "NEGOCIO_LIMITE_INTENTOS":            InternalError("BU001", "Alerta", "Error, Se ha superado el número de intentos.",                          False, HTTPStatus.ACCEPTED)
        }

    def get_error(self, param, return_type=None):
        if param in self.errors:
            return_type = c.copy(self.errors[param])
        return return_type

    def get_error_dict(self, wrapper, return_type=None):
        if wrapper['key'] in self.errors:
            return_type = c.copy(self.errors[wrapper['key']])
            if wrapper['key'] is 'NEGOCIO':
                # optional value for get_business_error.
                if wrapper['error'].internal is None:
                    wrapper['error'].internal = return_type.internal
                # optional value for get_business_error and if exists.
                if not getattr(wrapper['error'], 'detail', None) is None:
                    return_type.detail = wrapper['error'].detail
                return_type = wrapper['error']
            else:
                return_type.message = return_type.message.replace('{Campo}', wrapper['field'])
        return return_type
