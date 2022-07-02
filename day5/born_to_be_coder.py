n,m =input().split(' ')
pattern = '.|.'
green="\u001b[32m"
red= "\u001b[31m"
print(green)
for i in range(int(n)//2):
    print((pattern*(2*(i+1)-1)).center(int(m),'-'))
print(red,end='')
print("BORN TO BE CODER".center(int(m),'-'))
print(green,end='')
for i in range(int(n)//2):
    print((pattern*(2*((int(n)//2)-i)-1)).center(int(m),'-'))