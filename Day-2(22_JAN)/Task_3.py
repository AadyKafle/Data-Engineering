from abc import ABC, abstractmethod

class Employee(ABC):
    company_name = "TechCorp Pvt Ltd"

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def calculate_salary(self):
        pass

    @abstractmethod
    def get_role(self):
        pass

    def work(self):
        print(f"{self.name} is working.")

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Role: {self.get_role()}")
        print(f"Company: {Employee.company_name}")
        print(f"Salary: {self.calculate_salary()}")


class FullTimeEmployee(Employee):
    def __init__(self, name, annual_salary, benefits):
        super().__init__(name)
        self.annual_salary = annual_salary
        self.benefits = benefits

    def calculate_salary(self):
        return self.annual_salary / 12

    def get_role(self):
        return "Full-Time Employee"

    def work(self):
        print(f"{self.name} works full-time.")

    def show_benefits(self):
        print(f"Benefits: {self.benefits}")

class Manager(FullTimeEmployee):
    def __init__(self, name, annual_salary, benefits, team_size, bonus_percentage):
        super().__init__(name, annual_salary, benefits)
        self.team_size = team_size
        self.bonus_percentage = bonus_percentage

    def calculate_salary(self):
        bonus = self.annual_salary * self.bonus_percentage / 100
        return (self.annual_salary + bonus) / 12

    def get_role(self):
        return "Manager"

    def work(self):
        print(f"{self.name} manages a team of {self.team_size} people.")

    def conduct_meeting(self):
        print("Conducting team meeting.")


class Director(Manager):
    def __init__(self, name, annual_salary, benefits, team_size, bonus_percentage, department, additional_stock_options):
        super().__init__(name, annual_salary, benefits, team_size, bonus_percentage)
        self.department = department
        self.additional_stock_options = additional_stock_options

    def calculate_salary(self):
        base_salary = super().calculate_salary()
        return base_salary + self.additional_stock_options

    def get_role(self):
        return "Director"

    def work(self):
        print(f"{self.name} oversees the {self.department} department.")

    def approve_budget(self):
        print("Budget approved.")

class ContractEmployee(Employee):
    def __init__(self, name, hourly_rate, hours_worked, contract_duration):
        super().__init__(name)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked
        self.contract_duration = contract_duration

    def calculate_salary(self):
        return self.hourly_rate * self.hours_worked

    def get_role(self):
        return "Contract Employee"

    def work(self):
        print(f"{self.name} works on a contract basis.")

    def contract_details(self):
        print(f"Contract duration: {self.contract_duration} months")



fte = FullTimeEmployee("Aaditya", 1200000, ["Health Insurance", "Paid Leave"])
manager = Manager("Aryan", 1800000, ["Health Insurance", "Bonus"], 8, 10)
director = Director("Bigyan", 2500000, ["All Benefits"], 15, 20, "Engineering", 50000)
contractor = ContractEmployee("Ravi", 50, 160, 6)



employees = [fte, manager, director, contractor]

for emp in employees:
    emp.display_info()
    emp.work()
    print("-" * 40)


print(Director.mro())
