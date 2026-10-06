def calculate_gross_salary(basic_salary, allowance):
    return basic_salary + allowance


def calculate_tax(gross_salary):
    return gross_salary * 0.05


def calculate_net_salary(gross_salary, tax):
    return gross_salary - tax


employee_name = input("Enter Employee Name: ")
basic_salary = float(input("Enter Basic Salary: "))
allowance = float(input("Enter Allowance: "))

gross_salary = calculate_gross_salary(basic_salary, allowance)
tax = calculate_tax(gross_salary)
net_salary = calculate_net_salary(gross_salary, tax)

print("\n----- Employee Salary Details -----")
print("Employee Name:", employee_name)
print("Basic Salary:", basic_salary)
print("Allowance:", allowance)
print("Gross Salary:", gross_salary)
print("Tax (5%):", tax)
print("Net Salary:", net_salary)
