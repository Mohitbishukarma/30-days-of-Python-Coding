length = int(input("How many numbers do you want to sort? "))
nums = []
for i in range(length):
    num  = int(input(f"Enter Num {i+1} : "))
    nums.append(num)

for i in range(length):
    for j in range(length-i-1):
        if nums[j] > nums[j+1]:
            nums[j],nums[j+1] = nums[j+1],nums[j]
print(nums)
