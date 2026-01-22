import datetime
import re

class Employee:
    # Class variables
    company = "GrowByData"
    employees = []
    department_counts = {}
    _id_counter = 1

    def __init__(self, name, email, salary, department):
        self.name = name
        self.email = email
        self.salary = salary
        self.department = department

        # Generate employee ID
        self.employee_id = self.generate_employee_id()

        # Track employee
        Employee.employees.append(self)

        # Track department count
        if department in Employee.department_counts:
            Employee.department_counts[department] += 1
        else:
            Employee.department_counts[department] = 1

    @classmethod
    def change_company(cls, new_name):
        """
        Change company name after validation.
        """
        if not (3 <= len(new_name) <= 50):
            raise ValueError("Company name must be between 3 and 50 characters")

        if not re.match(r'^[A-Za-z0-9 ]+$', new_name):
            raise ValueError("Company name can contain only letters, numbers, and spaces")

        cls.company = new_name

    @classmethod
    def generate_employee_id(cls):
        """
        Generates unique ID in format EMP-YYYY-XXXX
        """
        year = datetime.datetime.now().year
        emp_id = f"EMP-{year}-{cls._id_counter:04d}"
        cls._id_counter += 1
        return emp_id
