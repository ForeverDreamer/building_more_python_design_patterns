from .abs_facade import AbsFacade


class MongoDb(AbsFacade):
    def get_employees(self):
        print('MongoDb get_employees')

    def create_employees(self):
        print('MongoDb create_employees')

    def update_employees(self):
        print('MongoDb update_employees')

    def delete_employees(self):
        print('MongoDb delete_employees')

