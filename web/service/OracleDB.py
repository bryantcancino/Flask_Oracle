import cx_Oracle


class OracleDB:
    """
    Usage:
        db = OracleDB("user", "pass", "yourserver.com", 1523, "YOUR_SID")
        db.connect()
        db.cursor.execute("SELECT yourcolumn FROM yourtable")
        result1 = [x[0] for x in db.cursor]
        db.close()
        db.connect()
        db.cursor.execute("SELECT yourothercolumn FROM yourothertable")
        result2 = [x[0] for x in db.cursor]
        db.close()
        # do stuff with result1 and result2 ...

		    cur = connection.cursor()
		    PCUR_OTORGANTE = cur.var(cx_Oracle.CURSOR)
		    PMENSAJE_ERROR = cur.var(cx_Oracle.STRING)
		    l_query = cur.callproc("CCSP_OBTIENE_OTORGANTE", [PCUR_OTORGANTE, PMENSAJE_ERROR])
		    l_results = l_query[0]
		    print(dir(l_results)) 
		    # lst = list(l_results)
		    response = []
		    for cell in l_results:
		        newNode = {
		                'NUMERO_OTORGANTE':cell[0],
		                'RAZON_SOCIAL':cell[1]
		        }
		        response.append({cell[0] : newNode})
		        # print(response)
		    my_json_string = json.dumps(response)
		    cur.close()
		    connection.close()            
    """
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



