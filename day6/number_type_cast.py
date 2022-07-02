import math

def print_formatted(number):
    max_length = math.floor(math.log(n, 2)) + 1

    for i in range(1, n+1):
        d = str(i).rjust(max_length)
        o = str(oct(i))[2:].rjust(max_length)
        h = str(hex(i))[2:].upper().rjust(max_length)
        b = bin(i)[2:].lstrip('0').rjust(max_length)
        print('{} {} {} {}'.format(d,o,h,b))
      

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)