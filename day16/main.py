from functools import reduce
myNums = [1,2,3]
sum = reduce(lambda x,y: x**y,  myNums )
print(sum)