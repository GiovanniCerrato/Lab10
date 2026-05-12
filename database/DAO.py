from database.DB_connect import DBConnect
from model.country import Country


class DAO():
    def __init__(self):
        pass

    @staticmethod
    def getAllCountry():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select *
                   from country c"""

        cursor.execute(query)

        for row in cursor:
            result.append(Country(**row))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAllNodes(x):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor()
        query = """SELECT c.state1no AS nodi
                    FROM contiguity c
                    WHERE c.`year` <= %s
                    
                    UNION
                    
                    SELECT c.state2no AS nodi
                    FROM contiguity c
                    WHERE c.`year` <= %s;"""

        cursor.execute(query, (x,x,))

        for row in cursor:
            result.append(row)

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAllEdges(x):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor()
        query = """select state1no,state2no 
                    from contiguity
                    where year <=%s and conttype = 1"""

        cursor.execute(query, (x,))

        for row in cursor:
            result.append(row)

        cursor.close()
        conn.close()
        return result
