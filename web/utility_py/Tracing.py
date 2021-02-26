import aspectlib
import inspect
import logging

@aspectlib.Aspect(bind=True)
def LoggerAspect(cut_point, *args, **kwargs):
    max_length = 80
    single_types = (int, str, float, complex)
    logger = logging.getLogger()

    frame = inspect.currentframe()
    args_info = inspect.getargvalues(frame)
    args_tuple = ""
    comma = False

    if type(args_info.locals.get('args')) is tuple:
        for ar in args_info.locals.get('args'):
            if comma:
                args_tuple += ", "
            if not isinstance(args_info.locals.get('args'), single_types):
                if len(str(ar)) > max_length:
                    args_tuple += str(ar)[:max_length]+"..."
                else:
                    args_tuple += str(ar)
            else:
                args_tuple += type(ar).__name__ +":"+str(ar.__dict__)
            comma = True
    else:
        args_tuple += str(args_info.locals.get('args'))
    logger.info("#####INICIA OPERACION### %s(%s)" % (cut_point.__name__, args_tuple))
    result = yield
    logger.info("#####CIERRA OPERACION### %s" % (cut_point.__name__))