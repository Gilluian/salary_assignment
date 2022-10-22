from ahall_assignment1_person import Person


class Employee(Person):

    def __init__(self, first, last, ssn, emp_id):
        super().__init__(first, last, ssn)
        self.emp_id = emp_id

    def __str__(self):
        return f'{super().__str__()}, ID: {self.emp_id}'
