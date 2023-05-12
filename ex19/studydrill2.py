# An extra function written and ran 10 more different ways:

def sum_even_nums(nums):
    total = 0
    for num in nums:
        if num % 2 == 0:
            total += num
    return total
# Now that we have defined our function, lets run it in 10 different ways:
#1:
print(sum_even_nums([1,2,3,4,5,6])) # output 12 
#2:
nums = [2,4,6,8]
print(sum_even_nums(nums)) # Output 20
#3
print(sum_even_nums([0,-2,4,-6])) #Output -4
#4:
print(sum_even_nums([])) # output 0
#5:
print(sum_even_nums([1,3,5])) # output 0
#6:
print(sum_even_nums([10])) # output 10
#7:
print(sum_even_nums([2,3,4,5,6])) # output 12
#8:
nums = [1,2,3,4,5,6,7,8,9,10]
print(sum_even_nums(nums[2:7])) # output 10
#9:
print(sum_even_nums([2.5,3.5,4.5,5.5])) # output 0
#10:
#print(sum_even_nums(['a','b','c','d'])) # output: not all arguments converted during string formation
#bonus:
a = 2
b = 4
c = 6
d = 8
print(sum_even_nums([a,b,c,d])) # output 20