# iterable is something which can be traversed
# iterable uses  iter() and returns iterator object
# next function is called using iterator

list1 = [1, 2, 3, 4, 5]
tupe1 = (1, 2, 3, 4, 5)

iterator = iter(list1)
iterator1 = iter(tupe1)

print(iterator)
print(iterator1)
print('printing list values......')
for i in range(len(list1)):

    print(next(iterator))

print('printing list values finished......')
print('printing tuple values')
for j in range(len(tupe1)):

    print(next(iterator1))
print('printing tuple values finished......')



