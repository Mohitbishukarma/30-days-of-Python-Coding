# binary to decimal and decimal to binary:
def binary_to_decimal(binary:str):
    length=len(binary)
    decimal=0
    for i in range(length):
        decimal+=int(binary[i])*2**(length-(i+1))
    return decimal

def decimal_to_binary(decimal):
    binary=[]
    while True:
        if decimal//2==1:
            binary.append("1")
            break
        if decimal%2==0:
            binary.append("0")
            decimal//=2
        else:
            binary.append("1")
            decimal//=2
    binary.reverse()
    return ''.join(binary)
b="100"
d=4
print(binary_to_decimal(b))
print(decimal_to_binary(d))
