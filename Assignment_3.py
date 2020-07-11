while True:
    number = input('Please enter a positve integer number')
    if not number.isdigit():
        print('Enter a positive number or 0')
        continue
    n=len(number)
    total=0
        #total = int(number[0])**n + int(number[1])**n+ int(number[2])**n +int(number[3])**n
    for i in range(n):
        total += int(number[i])**n
        #print(total)
    if int(number) == total:
        print(number,'this is a armstrong number')
        break