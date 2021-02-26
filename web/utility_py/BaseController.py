from flask import jsonify
from utility_py.GenericResponse import GenericResponse, SuccessMessage, Response, InternalError

class BaseController:
    
    def __init__(self):
        pass
        
    def success(self, data, messageTitle, message, status_code=200):
        success = SuccessMessage(messageTitle, message)
        return jsonify(self.get_response_success(True, [], success, data)), status_code

    def error(self, errors):
        error_list = []
        status_code = None
        for error in errors:
            status_code = error.status.__dict__.get('_value_')
            error.status = error.status.__dict__.get('_name_')
            error_list.append(error.__dict__)
        return jsonify(self.get_response_error(False, error_list)), status_code

    @staticmethod
    def get_response_success(isSuccess=None, errors=None, success=None, data=None):
        return GenericResponse(Response(isSuccess, success.__dict__, errors, data).__dict__).__dict__

    @staticmethod
    def get_response_error(isSuccess=None, errors=None, success=None, data=None):
        return GenericResponse(Response(isSuccess, success, errors, data).__dict__).__dict__
