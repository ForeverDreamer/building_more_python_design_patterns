from .abs_employees import AbsEmployees
from .access_controls import AccessControls
from .employee import Employee


class Proxy(AbsEmployees):

    def __init__(self, employees, reqid):
        self._employees = employees
        self._reqid = reqid

    def get_employee_info(self, empids):
        reqid = self._reqid
        acc = AccessControls.get_access_control()

        for e in self._employees.get_employee_info(empids):

            if e.empid == reqid or (reqid in acc and acc[reqid].can_see_personal):

                # Show everything
                yield Employee(e.empid, e.name,
                               ('%.2f' % e.salary),
                               e.birthdate)

            else:  # Hide birthdate and salary detailsd
                yield Employee(e.empid, e.name, '*****', '*****')
