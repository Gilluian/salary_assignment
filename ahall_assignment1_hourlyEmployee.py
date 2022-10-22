from ahall_assignment1_employee import Employee


class HourlyEmployee(Employee):

    def __init__(self, first, last, ssn, emp_id, hourly_rate, hours_per_week):
        super().__init__(first, last, ssn, emp_id)
        self.hourly_rate = hourly_rate
        self.hours_per_week = hours_per_week

    def weekly_pay(self):
        return round(self.hourly_rate * self.hours_per_week, 2)

    def __str__(self):
        return f'{super().__str__()}, Weekly Salary: ${self.weekly_pay()}'

