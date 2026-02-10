print("HELLO☺️👋🏻")
while True :
    print("please select an operation 👇🏻:")
    op = input("choose (+) (-) (×) (÷) (Quit for exsiting) :")
    if op == "+":
        print("enter your valeus:")
        A = float(input("A="))
        B = float(input("B="))
        C = A+B
        print("the result is =",C)
    elif op == "-":
        print("enter you valeus :")
        A = float(input("A="))
        B = float(input("B="))
        C = A-B
        print("the result is =",C)
    elif op == "×":
        print("enter your valeus :")
        A = float(input("A="))
        B = float(input("B="))
        C = A*B
        print("the result is =",C)
    elif op == "÷":
        print("enter your valeus :")
        A = float(input("A="))
        B = float(input("B="))
        if B == 0:
            print ("Division on Zero in not allowed !😥")
        else :
            C = A/B
            print("the result is =",C)
    elif op == "Quit":
        print("thank you for using the calculator 👋🏻🌹")
        break
    else:
        print("invalid operation selected !🙁")
