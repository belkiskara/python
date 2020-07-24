exact_list = [1,2,4,6]
while True:
 first_num = int(input("Please enter a first number"))
 if first_num > len(exact_list):
     print("Out of range")
     continue
 else:
     print(exact_list[first_num])
 second_num = int(input("Please enter a second number"))
 if second_num > len(exact_list):
     print("Out of range")
     continue 
 else:
     print(exact_list[second_num])
     print(exact_list[first_num], ",", exact_list[second_num])



#solution_2
# list1 = [1,2,4,6]
# x = 0
# y = int(input("Please enter a number"))
# # for i in list1:
#     if y <= len(list1):
#         print(f'{i} is in the {x} index')
#     else:
#         print("You write an invalid number")
#     x += 1
#     break