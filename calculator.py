num1=int(input("enter a integer:"))
num2=int(input("enter another integeer:"))

operation = input("enter the operation you want to perform '+' '-' '*' '/' '%' '**'")
if operation=="+":
    print("answer is:", num1+num2)
elif operation=="-":
    print("answer is:", num1-num2)
elif operation=="*":
    print("answer is:", num1*num2)
elif operation=="/":
    print("answer is:", num1/num2)
elif operation=="%":
    print("answer is:", num1%num2)
elif operation=="**":
    print("answer is:", num1**num2)