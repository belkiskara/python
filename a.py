while True :
    number = (input("\nPlease Enter the Number to Check for Armstrong: "))
    sum1=0

    if ("," in number) or ("." in number) :
        print("Please enter an integer number")
    elif int(number) < 0:
        print("Please enter positive number")
    elif not number.isdigit():
        print("Dont use any entries other than numeric values")
    else:
        for i in range(len(number)):
         sum1 += int(number[i]) ** len(number)
        if sum1 == int(number):
            print(number, "is an Armstrong number")
            break
        else:
            print( number, "is not an Armstrong number")
            break
        
         
