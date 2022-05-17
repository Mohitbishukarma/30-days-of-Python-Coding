def max_min(numbers:list):
    numbers.sort()
    return numbers[-1],numbers[0]
numbers=[3,4,2]
(max,min)=max_min(numbers)
print(f"Max : {max} \nMin : {min}")

