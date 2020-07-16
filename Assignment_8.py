while True:
 ly = input('Please enter a year: ').strip()
 if not ly.isdigit():
  print('Please enter a digit number: ')
  continue 
 if (int(ly)%4 == 0 or int(ly)%400 == 0) and int(ly)%100 != 0:
  print(f'this {ly} year is a leap year')
  break  
 else:
  print(f'This {ly} year is not a leap year') 
  break



#solution 2

# year = int(input("Dort rakamli bir yil giriniz :"))
# leap = (year % 4 == 0) and ((year % 100 == 0) or (year % 100 != 0))
# print(leap)