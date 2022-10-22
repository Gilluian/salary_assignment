class Person:

    def __init__(self, first, last, ssn):
        self.first = first
        self.last = last
        self.ssn = ssn

    def __str__(self):
        return f'Name: {self.first} {self.last}, SSN: {self.ssn}'

