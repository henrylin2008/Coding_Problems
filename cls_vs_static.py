class Employee:

    num_of_emps = 0
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@email.com'

        Employee.num_of_emps += 1

    def fullname(self):
        return f'{self.first} {self.last}'

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    @classmethod    # like a constructor, build on top of inits
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

    @classmethod    # constructor to split input string with '-'
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod   # no access to class or object instance at all, isolated from everything else
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


emp1 = Employee('C', 'S', 50000)
emp2 = Employee('T', 'E', 60000)

e1 = 'John-Doe-70000'
e2 = 'Steve-Jobs-30000'
e3 = 'Steph-Curry-50000'

# new_e1 = Employee.from_string(e1)  //test from classmethod

# print(new_e1.email)   //test from classmethod
# print(new_e1.pay) //test from classmethod
# Employee.set_raise_amt(1.05)
# print(Employee.raise_amt)
# print(emp1.raise_amt)
# print(emp2.raise_amt)
# import datetime                       //test for statismethod
# my_date = datetime.date(2016, 7, 10)  //test for statismethod
# print(Employee.is_workday(my_date))   //test for statismethod