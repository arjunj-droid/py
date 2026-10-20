#division
num1 =float(input("Enter the first number for division:"))
num2 =float(input("Enter the second number for division:"))
if num2 == 0:
    print("Enter the second number other than 0")
else:
    div_result=num1/num2
    print(f"the division:{num1}/{num2}={div_result}")