sentence = input("Please enter a sentence").strip()
count_num = {}
for i in sentence:
  if i == ' ':
   continue
  count_num.update({i:sentence.count(i)}) 
print(count_num)
