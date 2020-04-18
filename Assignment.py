year = int(input("Dort rakamli bir yil giriniz :"))
leap = (year % 4 == 0) and ((year % 100 == 0) or (year % 100 != 0))
print(leap)
