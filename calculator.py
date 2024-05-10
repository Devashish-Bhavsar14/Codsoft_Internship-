num1=int(input("enter the first number : ="))
sign=input(" enter the operation: +,-,*,/ =")
num2=int(input("enter the second number: ="))

match sign:
    case '+':
     result=num1+num2
    case '-':
     result=num1-num2
    case '*':
     result=num1*num2
    case '/':
     result=num1/num2
    case "_":
        print("wrong input")
    
print(f"result of two number {num1} and {num2} is= {result}")
