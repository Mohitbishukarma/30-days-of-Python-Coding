"""
    python: 3.10.1
    coder: Mohit Bk
"""
n,m =input().split(' ')
pattern = '.|.'
for i in range(int(n)//2):
    print((pattern*(2*(i+1)-1)).center(int(m),'-'))
print("WELCOME".center(int(m),'-'))
for i in range(int(n)//2):
    print((pattern*(2*((int(n)//2)-i)-1)).center(int(m),'-'))

"""
<-----input---->
n: an integer (must be an odd number)
m: an integer (three times of n)
<-----output------>
size 7x21:
---------.|.---------
------.|..|..|.------
---.|..|..|..|..|.---
-------WELCOME-------
---.|..|..|..|..|.---
------.|..|..|.------
---------.|.---------
"""