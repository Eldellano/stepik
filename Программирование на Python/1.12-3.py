a = float(input())
b = float(input())
oper = str(input())

if (oper == "+"):
    print(a + b)
elif (oper == "-"):
    print(a - b)
elif (oper in ("/", "mod", "div")) and (b == 0):
    print("Деление на 0!")
elif (oper == "/"):
    print(a/b)
elif (oper == "*"):
    print(a * b)
elif (oper == "mod"):
    print(a % b)
elif (oper == "pow"):
    print(a ** b)
elif (oper == "div"):
    print(a // b)
