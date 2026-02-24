class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_person(self):
        print("Name:", self.name)
        print("Age:", self.age) 

class employee:
    def __init__(self, emp_id, salary):
        self.emp_id = emp_id
        self.salary = salary

    def display_employee(self):
        print("Employee ID:", self.emp_id)
        print("Salary:", self.salary)

class manager(person, employee):
    def __init__(self, name, age, emp_id, salary, department):
        person.__init__(self, name, age)
        employee.__init__(self, emp_id, salary)
        self.department = department

    def display_manager(self):
        self.display_person()
        self.display_employee()
        print("Department:", self.department)

m1 = manager("Sagar", 20, 101, 50000, "cse")
m1.display_manager()