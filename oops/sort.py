list1= [1,3,2,5,100,0]

for i in range(len(list1)):
  pos1 = list1.index(list1[i])
  for j in range(len(list1)):
    pos2= list1.index(list1[j])
    if list1[i] > list1[j]:
      temp = list1[pos1]
      list1[pos1] = list1[pos2]
      list1[pos2] = temp
    else:
      pass

print(list1)

# [100, 5, 3, 2, 1, 0]
