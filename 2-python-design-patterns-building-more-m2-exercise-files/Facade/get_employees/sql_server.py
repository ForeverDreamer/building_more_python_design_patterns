# import pyodbc
from .abs_facade import AbsFacade
from . import CONNSTR, QUERY


class SqlServer(AbsFacade):
    def get_employees(self):
        print('SqlServer get_employees')
        # connection = pyodbc.connect(CONNSTR)
        # cursor = connection.cursor()
        # cursor.execute(QUERY)
        # for row in cursor:
        #     print(row.FirstName, row.LastName)
        # connection.commit()
        # connection.close()

    def create_employees(self):
        print('SqlServer create_employees')

    def update_employees(self):
        print('SqlServer update_employees')

    def delete_employees(self):
        print('SqlServer delete_employees')

