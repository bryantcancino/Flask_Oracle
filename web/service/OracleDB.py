import cx_Oracle


class OracleDB:
    def __init__(self, user, password, server, port, sid):
        self.tns = cx_Oracle.makedsn(server, port, sid)
        self.connection = None
        self.cursor = None
        self.user = user
        self.password = password

    def connect(self):
        self.connection = cx_Oracle.connect(self.user, self.password, self.tns)
        self.cursor = self.connection.cursor()

    def close(self):
        self.cursor.close()
        self.connection.close()



