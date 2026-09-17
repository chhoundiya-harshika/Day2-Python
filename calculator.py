while True:
    print("1.ADD")
    print("2.SUB")
    print("3.MUL")
    print("4.DIV")
    print("5.exit")

    choice = int(input("Enter a choice"))

    match choice:
        case 1:
            a=int(input("enter num1"))
            b=int(input("enter num2"))
            def ADD(a,b):
                print("Addition:",a+b)
            ADD(a,b)
        case 2:
            a=int(input("enter num1"))
            b=int(input("enter num2"))
            def SUB(a,b):
                print("subtraction:",a-b)
            SUB(a,b)
        case 3:
            a=int(input("enter num1"))
            b=int(input("enter num2"))
            def MUL(a,b):
                print("MULTIPLICARION:",a*b)
            MUL(a,b)
        case 4:
            a=int(input("enter num1"))
            b=int(input("enter num2"))
            def DIV(a,b):
                print("division:",a/b)
            DIV(a,b)
        case 5:
            print("enter proper input")
            break
        case _ :
            print("invalid choice")
        
        