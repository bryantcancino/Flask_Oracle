class GenericResponse:

    def __init__(self, response=None):
        self.response = response


class SuccessMessage:

    def __init__(self, title=None, message=None):
        self.title = title 
        self.message = message


class Response:
    
    def __init__(self, isSuccess=None, success=None, errors=None, data=None):
        self.isSuccess = isSuccess
        self.success = success
        self.errors = errors
        self.data = data

class InternalError(object):

    def __init__(self, code, title, message, internal=False, status_code_object=None, detail=None):
        self.code = code
        self.title = title
        self.message = message
        self.internal = internal
        self.status = status_code_object
        if detail is not None:
            self.detail = detail