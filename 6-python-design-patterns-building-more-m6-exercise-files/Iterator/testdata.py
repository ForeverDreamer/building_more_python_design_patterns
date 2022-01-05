from datetime import datetime as dt
from employee import Employee
from employee_collection import Employees
from department import Department
from department_collection import Departments

TESTEMPLOYEES = (
    (1, 'Douglas Adams', dt(1942, 7, 6)),
    (2, 'Sherlock Holmes', dt(1887, 3, 15)),
    (3, 'Albert Einstein', dt(1915, 11, 25)),
    (4, 'Sir John A Macdonald', dt(1867, 8, 1)),
    (5, 'Theodore Roosevelt', dt(1901, 9, 14))
)

employees = Employees()
for number, name, date in TESTEMPLOYEES:
    employees.add_employee(
        Employee(number, name, date)
    )

TESTDEPARTMENTS = (
    (101, 'Sci-Fi Commedy', dt(2010, 10, 1)),
    (102, 'Mystery', dt(2012, 2, 13)),
    (103, 'Physics', dt(2014, 5, 14)),
    (104, 'Politics', dt(2016, 7, 28)),
    (201, 'POTUS', dt(1776, 7, 4))
)

departments = Departments()
for number, name, date in TESTDEPARTMENTS:
    departments.add_department(
        Department(number, name, date)
    )
