a = float(input("Enter number 1 :"))
b = float(input("Enter number 2 :"))

print("Press 1 for addition\nPress 2 for subtraction\nPress 3 for muliplication\nPress 4 for division")

operation =  int(input("Enter your desired arithematic operation from 1-4 : "))

if(operation == 1):
    print("Result :",a + b)
elif(operation == 2):
    print("Result :",a-b)
elif(operation == 3):
    print("Result :",a*b)
elif(operation == 4):
    if(b != 0):
        print("Result :",a/b)
else:
    print("Invalid input")