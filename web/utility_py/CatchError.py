import logging

from utility_py.BaseController import BaseController
from utility_py.Colors import Colors as c
from utility_py.Errors import Errors


class CatchError(object):

    def __init__(self, error_return=None):
        self.error_return = error_return
        format_colors = c.dictionary.get("WHITE")+'%(asctime)s '+c.dictionary.get("NULL") \
            + c.dictionary.get("BLUE")+'%(levelname)7s ' + c.dictionary.get("NULL") \
            + c.dictionary.get("MAGENTA")+'%(process)5d ' + c.dictionary.get("NULL") \
            + c.dictionary.get("CYAN") + '%(filename)20s ' + c.dictionary.get("NULL") \
            + '%(message)s'
        logging.basicConfig(format=format_colors, level=logging.INFO)
        self.logger = logging.getLogger()
        self.utility_errors = Errors()

    def __call__(self, function):
        def wrapper_function(*args, **kwargs):
            errors_to_launch = []
            try:
                return function(*args, **kwargs)
            except Exception as get_exceptions:
                """
                :param get_exceptions: could be a tuple with multiple error types or 
                could be an array with errors from utility
                
                If the first argument is a list, the errors come from utility tool. In other way,
                the errors could be from an unknown source.
                """
                if type(get_exceptions) is Exception:
                    # if length is 0 was like raise Exception()
                    if len(get_exceptions.args) == 0:
                        errors_to_launch.append(self.utility_errors.get_error('GENERAL_GENERICO_PUBLICO'))
                        self.logger.error("#####ERROR### " + str(errors_to_launch[-1].__dict__))
                    # in case length > 0, could be Excception(['E1', 'E2', ..., 'En']) or Exception("E1", "E2", ..., "En")
                    else:
                        for arguments in get_exceptions.args:
                            # if type is list, maybe are exceptions from utility.
                            if type(arguments) is list:
                                for single_exception in arguments:
                                    # if the type of exception is a dictionary then was exception managed from utility
                                    if type(single_exception) is dict:
                                        errors_to_launch.append(self.utility_errors.get_error_dict(single_exception))
                                        self.logger.error("#####ERROR### " + str(errors_to_launch[-1].__dict__) )
                                    # could be general exception or unexpected.
                                    else:
                                        errors_to_launch.append(self.utility_errors.get_error('GENERAL_GENERICO_PUBLICO'))
                                        self.logger.error("#####ERROR### " + str(errors_to_launch[-1].__dict__))
                                        break
                            # otherwise are general exceptions or unexpected.
                            else:
                                errors_to_launch.append(self.utility_errors.get_error('GENERAL_GENERICO_PUBLICO'))
                                self.logger.error("#####ERROR### " + str(errors_to_launch[-1].__dict__))
                                break
                # unexpected errors are managed here
                else:
                    errors_to_launch.append(self.utility_errors.get_error('GENERAL_GENERICO_PUBLICO'))
                    self.logger.error("#####ERROR### " + str(get_exceptions))
                self.error_return = BaseController().error(errors_to_launch)
            return self.error_return
        return wrapper_function