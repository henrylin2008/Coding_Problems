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

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)


emp1 = Employee('C', 'S', 50000)
emp2 = Employee('T', 'E', 60000)

e1 = 'John-Doe-70000'
e2 = 'Steve-Jobs-30000'
e3 = 'Steph-Curry-50000'

new_e1 = Employee.from_string(e1)

print(new_e1.email)
print(new_e1.pay)
# Employee.set_raise_amt(1.05)
#
# print(Employee.raise_amt)
# print(emp1.raise_amt)
# print(emp2.raise_amt)
