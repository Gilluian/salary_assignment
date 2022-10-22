# ahall_assignment1_main.py

from ahall_assignment1_hourlyEmployee import HourlyEmployee
from ahall_assignment1_employee import Employee
from ahall_assignment1_salaryEmployee import SalaryEmployee


def main():

    # Demonstrating an employee
    chatterbox = Employee('Charles', 'Chatterbox', '234-54-4333', 1)
    print(chatterbox)
    print(f"{chatterbox.last} doesn't earn a paycheck. But he is employee #{chatterbox.emp_id}.\n")

    # Demonstrating hourly employee
    gunner = HourlyEmployee("William", "Gunner", '123-45-6789', 2, 24.08, 40)
    print(gunner)
    print(f'{gunner.first} {gunner.last} is an hourly employee who earns ${gunner.weekly_pay()} per week.\n')

    # Demonstrating Salary employee
    wrangler = SalaryEmployee("Randy", "Wrangler", "573-11-6596", 3, 4200)
    print(wrangler)
    print(f'{wrangler.first} is a salaried employee who earns ${wrangler.get_yearly_salary()} per year. '
          f'Or, ${wrangler.get_monthly_salary()} per month.')


if __name__ == '__main__':
    main()
