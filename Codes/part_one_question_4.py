# getting salary
salary = int(input("Enter salary of employee: "))

# calculate tax
tax = salary*(9/100)

# calculate insurance
insurance = salary*(7/100)

# calculate final Salary
print(f"Final: {salary - tax - insurance}")