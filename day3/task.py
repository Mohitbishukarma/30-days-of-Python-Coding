# pattern
row=int(input("Enter Row :"))
col=int(input("Enter Column :"))
for i in range(row):
    print("* "*col)

# second largest num
_list=[2,4,2,45,3,22,45]
_list.sort()
_secondBigDigit=0
for i in _list:
    if i>_secondBigDigit and i<_list[-1]:
        _secondBigDigit=i
print(_secondBigDigit)

# mean of arr
_list=[20,10]
print(sum(_list)/len(_list))

# arr to str:
arr=['m','o','h','i','t']
print("".join(arr))

# product of odd nums:
_list=[1,2,3]
oddNums=[num for num in _list if num%2!=0]
product=1
for num in oddNums:
    product*=num
print(product)


# vowel, consotants counter
def vowel_consotant(s):
    vowel="aeiou"
    vowelLtr=0
    consotantLtr=0
    for char in s:
        if char in vowel:
            vowelLtr+=1
        else:
            consotantLtr+=1
    return vowelLtr,consotantLtr
vowel,consotant=vowel_consotant("mohit")
print(f"Vowel Letters : {vowel} \nConsotants Letters : {consotant}")


