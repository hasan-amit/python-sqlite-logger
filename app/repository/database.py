import sqlite3
from sqlite3 import Error
from pathlib import Path

class SqliteDatabse:
    """ 
    Create a connection with SQLite database.
    """
    def __init__(self, path=None) -> None:
        """ Create a connection with SQLite database specified
            by the mytest.db file
        :param db_path: the sqlite db file path
        :return: class  object instance its self internally"""
        self.path=path
        self.connection = None
        self.setup()
        pass

    def setup(self):
        """ Create a connection with SQLite database specified
            by the mytest.db file
        :return: connection object or Error"""
        try:
            if not self.path:
                self.path = f"{Path(__file__).resolve().parent}/sqlite.db"
            self.connection = sqlite3.connect(self.path)
        except Error:
            return None
    
    def execute(self, query:str, entity:tuple=None):
        """
        Execute query in database.
        :param query: sql query string 
        :param entity: tuple entity for query data
        :return: cursor the execution result
        """
        cur = self.connection.cursor()
        try:
            if entity:
                cur.execute(query, entity)
            else:
                cur.execute(query)
            self.connection.commit()
        except Error:
            print(Error)
            cur = None
        finally:
            return cur
    
    def close(self):
        """
        Close Database Connection.
        """
        self.connection.close()



class DataRepository(SqliteDatabse):
    def __init__(self, path=None) -> None:
        super().__init__(path)
        self.create_table()

    def isTableExists(self, tableName:str) -> bool:
        """
        Check if table is exists in database.
        :param tableName: the name of the table
        :return: table extsts status True or False
        """
        query_string ="""SELECT count(name) FROM sqlite_master WHERE type= ? AND name= ?"""
        cursor = self.execute(query_string, ('table','employees'))
        res = cursor.fetchone()[0]
        if res==1:
            return True
        return False

    def create_table(self):
        """
        Create the table with given columns
        """
        if not self.isTableExists(tableName="employees"):
            query_string = f"""CREATE TABLE employees(
                            id INTEGER PRIMARY KEY,
                            name TEXT,
                            surname TEXT,
                            department TEXT,
                            position TEXT,
                            salary REAL,
                            data JSON,
                            date TEXT);"""
            self.execute(query_string)

    def insert(self, entities:list):
        """
        Insert records into the table
        """
        query_string = """INSERT INTO employees (id, name, surname, department, position, salary, data, date) VALUES(?,?,?,?,?,?,?,?)"""
        for entity in entities:
            self.execute(query_string, entity)


    def select_all(self):
        """Selects all rows from the table to display
        """
        sql_string = 'SELECT * FROM employees'
        cur = self.execute(query=sql_string)
        rows = cur.fetchall()
        return rows


    def update(self, salary, id):
        """ Update the table with given new values"""

        sql = """UPDATE employees SET salary = ?  WHERE id = ?"""
        self.execute(sql, (salary, id))


    def delete(self, surname):
        """ Delete the given record
        """
        query = "DELETE FROM employees WHERE surname = ?;"
        self.execute(query, (surname,))