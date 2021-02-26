class InternalException:

    def __init__(self):
        self.exceptions = []
        pass

    def add(self, exception):
        if exception is not None:
            return self.exceptions.append(exception)
        return False

    def launch(self):
        if len(self.exceptions) > 0:
            raise Exception(self.exceptions)

        return False
