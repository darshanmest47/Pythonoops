def factorial(num):
    mul = 1
    for i in range(1, num + 1):
        mul = mul * i
        yield mul


nums = int(input('Please enter the number of whose factorial is needed'))

fact = factorial(nums)


for i in range(nums):
    print(next(fact))
