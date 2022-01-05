from get_employees import PROVIDER
from get_employees.db_connection_factory import DbConnectionFactory
"""Classification: Structural"""
"""sqlalchemy就是一种封装关系型数据库的外观模式(facade pattern)"""


def main():
    for db_name in ('mongodb', 'sql_server'):
        connection = DbConnectionFactory.create_connection(db_name)
        connection.create_employees()
        connection.get_employees()
        connection.update_employees()
        connection.delete_employees()


if __name__ == '__main__':
    main()
