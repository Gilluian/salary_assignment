# ahall_assignment1_salaryEmployee.py

# Alexander Hall
# 10/21/222
# Week 9 Assignment 1

from ahall_assignment1_employee import Employee


class SalaryEmployee(Employee):

    def __init__(self, first, last, ssn, emp_id, monthly_salary):
        super().__init__(first, last, ssn, emp_id)
        self.monthly_salary = monthly_salary

    def get_weekly_salary(self):
        return self.monthly_salary / 4

    def get_monthly_salary(self):
        return self.monthly_salary

    def get_yearly_salary(self):
        return self.monthly_salary * 12

    def __str__(self):
        return f'{super().__str__()} | Weekly Earnings: ${self.get_weekly_salary()} | ' \
               f'Monthly Earning: ${self.get_monthly_salary()} | ' \
               f'Yearly Earning: ${self.get_yearly_salary()}'
