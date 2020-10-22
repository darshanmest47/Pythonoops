# generators are the functions which return generator iterator using yield


def fibbo(nums):
    num1 = 0
    num2 = 1

    for i in range(nums):
        num3 = num1 + num2

        yield num3
        num1 = num2

        num2 = num3


nums = int(input('Please enter for how many numbers you need fibonnacci series'))
gen = fibbo(nums)

for i in range(nums):
    print(next(gen))
