age = int(input('Please enter your age'))
cronic = input('Do you have a severe chronic disease').lower().strip
immune = input('Is your immune system too weak?').lower().strip
if age > 75 or cronic == 'yes' or cronic == 'yes':
 print("You are in risky group")
else :
 print("You are not in risky group")