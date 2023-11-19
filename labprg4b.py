while True:
    var1=float(input("enter first variable: "))
    var2=float(input("enter second variable: "))
    op=input("Enter + to add\n- to subtract\n * for multiplication\n/ to divide\n type quit to exit")
    if(op=="+"):
        print(var1+var2)
    elif(op=="-"):
        print(var1-var2)
    elif(op=="*"):
        print(var1*var2)
    elif(op=="/"):
        print(var1/var2)
    elif(op=="quit"):
        break
    else:
        print("Invaild Input, please try again")
