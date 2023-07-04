# nums = range(1,10,2)
# print(type(nums))

# for i in range(1,10,2):
#     print(i)

#1 max num finding 
# nums = [2,4,3,5,3,6,2,8]
# print(max(nums))
# del nums

# 3 Code with mosh 

# def speed_check(speed):
#     demerits_point = 0
#     if speed < 70 :
#         print("OK")
#     elif speed > 70 :
#         extra_speed = speed -70
#         demerits_point += extra_speed // 5 
#         if demerits_point > 12 :
#             print("License suspended ")
#         else:
#             print(f"Points : {demerits_point}")


# speed_check(50)
# speed_check(73)
# speed_check(80)
# speed_check(180)


def showNums(limit):
    for i in range(0,limit+1):
        if i%2 == 0 :
            print(f"{i} EVEN")
        else:
            print(f"{i} ODD")

showNums(3)
print("--------------")
showNums(10)
print("--------------")
showNums(5)
print("--------------")


def sum_advanced(limit):
    _sum = 0
    for n in range(1,limit+1):
        if n % 3 == 0  or n % 5 == 0:
            _sum += n
    return _sum
print(sum_advanced(10))
print(sum_advanced(20))

def show_stars(rows):
    for i in range(rows):
        print("*"*(i+1))
show_stars(5)
show_stars(9)


def prime_detect(limit):
    for i in range(2,limit+1):
        is_prime = True
        for j in range(2,i):
            if i % j == 0 :
                is_prime = False
        if is_prime == True :
            print(i)
prime_detect(100)
        
