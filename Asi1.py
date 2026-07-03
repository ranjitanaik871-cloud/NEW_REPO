name=input("Employee name:")
id=int(input("Employee_id:"))
depar=input("Department:")
print("---------------------------------------------------\n")
print("SALARY DETAILS\n")
salary=float(input("Basic_Salary:"))
hra=float(input("HRA:"))
da=float(input("DA:"))
gross_salary=salary+hra+da
print("Gross_salary:",gross_salary)
Tax=float(input("Tax:"))
print("---------------------------------------------------\n")

net_salary=gross_salary-Tax
print("Net Salary:",net_salary)