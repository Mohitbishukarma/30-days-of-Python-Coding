# implemantation of all and any functions :

# all : returns true if all of the data in an iterable is true else false
print(all([True,False,True]))  # output : False
print(all([True,True,True]))  # output : True
print(all([]))  #output : True

# any : returns true if one of the data of an iterable is true else false
print(any([False, False ,True])) # output : True
print(any([False, False ,False])) # output : False
print(any([])) # output : False

# example
nums = [num for num in range(1,21)]

if all([num%2 == 0 for num in nums]):
    print("all numbers in nums are even")
if any([num%2 == 0 for num in nums]):
    print("at least one num is even in nums")

# enumerate function
# accessing index and value of list:
# method 1:
for num in nums:
    print(f"{nums.index(num)} : {num}")

# method 2:
for index , value in enumerate(nums):
    print("{0} : {1}".format(index, value))
