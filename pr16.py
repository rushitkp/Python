#Write a program in python to implement Salary printing file read operation. (File format: EmployeeNo, name,deptno, basic, DA, HRA, Conveyance) should perform below operations.
#a) Print Salary Slip for given Employee Number
#b) Print Employee List for Given Department Number

# Define a function to read employee salary details from a file
def read_employee_salary_details(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    employee_details = []
    for line in lines:
        employee_details.append(line.strip().split(','))
    return employee_details

# Define a function to print a salary slip for a given employee number
def print_salary_slip(employee_details, emp_no):
    for emp in employee_details:
        if emp[0] == emp_no:
            print(f"Employee Number: {emp[0]}")
            print(f"Name: {emp[1]}")
            print(f"Department Number: {emp[2]}")
            print(f"Basic Salary: {emp[3]}")
            print(f"DA: {emp[4]}")
            print(f"HRA: {emp[5]}")
            print(f"Conveyance: {emp[6]}")
            print(f"Total Salary: {float(emp[3]) + float(emp[4]) + float(emp[5]) + float(emp[6])}")
            return
    print(f"Employee with Employee Number {emp_no} not found.")

# Define a function to print an employee list for a given department number
def print_employee_list(employee_details, dept_no):
    print(f"Employee List for Department Number {dept_no}:")
    for emp in employee_details:
        if emp[2] == dept_no:
            print(f"Employee Number: {emp[0]}, Name: {emp[1]}")

# Read employee salary details from a file
employee_details = read_employee_salary_details('employee_salary.txt')

# Print salary slip for a given employee number
emp_no = input("Enter Employee Number to print Salary Slip: ")
print_salary_slip(employee_details, emp_no)

# Print employee list for a given department number
dept_no = input("Enter Department Number to print Employee List: ")
print_employee_list(employee_details, dept_no)
