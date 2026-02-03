class superhero:
    def __init__(self,name,crown_color):
        self.name=name
        self.crown_color=crown_color

    def fly(self):
        print(f"{self.name} is flying with a {self.crown_color}")

    
superman=superhero("superman","red")
print(superman.name)
print(superman.crown_color)
print(superman.fly())


# check if employee has achieved their weely target

#noun--employee--class
#adjective--name,designation,sales made
#verb--check if weekly target was achieved


class Employee:
    name='Arjun'
    designation='sales executive'
    salesMadeThisWeek=6

    def hasAchievedWeeklyTarget(self):
        if self.salesMadeThisWeek>=5:
            print("target is achieved")
        else:
            print("target is not achieved")
   


empOne=Employee()
print(empOne.name)
print(empOne.designation)
print(empOne.salesMadeThisWeek)
empOne.hasAchievedWeeklyTarget()

class Employee:
    def employeeDetails(self):
        pass

emp=Employee()
emp.employeeDetails()


class Employee:
    def employeeDetails(self):
        self.name = 'Arjun'
        self.age = 25
        print('Age', self.age)

    def printEmployeeDetails(self):
        print("Printing employee details in another method")
        print('Name of the employee:', self.name)
        print('Age of the employee:', self.age)  # Accessing variable local to employeeDetails

employee = Employee()
employee.employeeDetails()
employee.printEmployeeDetails()



class Employee:
    def employeeDetails(self):
        self.name='Ben'
    
    @staticmethod
    def welcomeMessage():
        print('welcome to the organisation')


emp=Employee()
emp.employeeDetails()
print(emp.name)
emp.welcomeMessage()


class Employee:
    def __init__(self):
        self.name="Arjun"

    def displayEmploeeDetails(self):
        print(self.name)

e=Employee()
e.displayEmploeeDetails()