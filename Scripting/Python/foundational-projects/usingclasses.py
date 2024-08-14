# class definition
class Employee:
    "Common base class for all employees"
    empCount = 0

    # class constructor
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1
    # define member methods
    def displayCount(self):
        print("Total Employee:", Employee.empCount)

    def displayEmployee(self):
        print("Name: ", self.name, ", Salary: ", self.salary)
# create instances by calling Employee()
"This would create first object of Employee class"
emp1 = Employee("Zara", 20000)
"This would create second object of Employee class"
emp2 = Employee("Manny", 50000)

# access objects' attributes
emp1.displayEmployee()
emp2.displayEmployee()
print("Total Employee: ", Employee.empCount)
