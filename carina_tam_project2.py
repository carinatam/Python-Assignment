#Project 2
print("This program will calculate your weekly pay and produce a pay slip showing your name, gross pay, deductions, and net pay")
print("Please do not enter any symbols such as \"$\" in the inputs")
f=input("Please enter your family name: ")
g=input("Please enter your given name: ")
h=float(input("Please enter your hourly rate of pay: "))
n=float(input("Please enter the number of hours you have worked this week: "))
t=input("Please enter your tax category;A=no tax deduction;B=tax is 10% of gross pay;C=tax is 20% of gross pay;D=tax is 29% or gross pay;E=tax is 35% of gross pay: ")
c=input("Please enter a Y for yes or N for no to whether or not you want $20 deducted from your weekly pay as a contribution to the United Way Charity: ")

#Gross pay for overtime
if(n>=41):
    m=n-40
    o=n-m
    hm=h*2
    gross_pay=(h*o)+(hm*m)
elif(n<=40):
    gross_pay=h*n

#Tax deductions
if(t=="A" or t=="a"):
    tax_deductions=gross_pay*0
elif(t=="B" or t=="b"):
    tax_deductions=gross_pay*0.1
elif(t=="C" or t=="c"):
     tax_deductions=gross_pay*0.2
elif(t=="D" or t=="d"):
    tax_deductions=gross_pay*0.29
elif(t=="E" or t=="d"):
    tax_deductions=gross_pay*0.35
    
#Charity deductions
if(c=="Y" or c=="y"):
    charity_deductions=20
elif(c=="N" or c=="n"):
    charity_deductions=0

#Add all deductions
deductions=tax_deductions+charity_deductions

#Subtract deductions from gross pay to get net pay
net_pay=gross_pay-deductions

#Pay slip
print("Name: ",g,f)
print("Gross pay: $",gross_pay)
print("Deductions: $",deductions)
print("Net pay: $",net_pay)
