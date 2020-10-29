num = 1002
rev = 0
temp = num
while num !=0:
  rev = (rev *10) + (num%10)
  
  num = int(num/10)
  
print (temp)
print(rev)
if temp == rev:
  print ('palindrome')
else:
  print('not a palindrome')
  
