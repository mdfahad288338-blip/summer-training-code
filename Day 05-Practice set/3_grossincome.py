# write a program to calculate gross salary of a family
income = []
for i in range(4):
    salary = float(input(f"Enter the salary of member {i+1}:"))
    income.append(salary)
gross_income = sum(income)
gst = gross_income*0.18   #assuming 18% GST
total_income = gross_income + gst
print(f"The gross income of family is:{gross_income}")
print(f"GST amount:{gst}")
print(f"Total income of family:{total_income}")