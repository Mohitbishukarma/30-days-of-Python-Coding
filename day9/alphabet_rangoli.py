def print_rangoli(size):
    alphabets = "abcdefghijklmnopqrstuvwxyz"
    side_alphabet = ""
    # top part
    for i in range(size):
        side_alphabet_to_use = ""
        for c in side_alphabet:
            if c == side_alphabet[-1]:
                side_alphabet_to_use += c
            else:
                side_alphabet_to_use += c+"-"
        print((side_alphabet_to_use+"-"+alphabets[size-(i+1)]+"-"+side_alphabet_to_use[::-1]).center((size*2-1)+(size*2-2),'-'))
        side_alphabet = side_alphabet+alphabets[size-(i+1)]  
    side_alphabet = side_alphabet.replace(side_alphabet[-1],'') 

    # bottom part
    for i in range(size-1):
        side_alphabet = side_alphabet.replace(side_alphabet[-1],'')
        side_alphabet_to_use = ""
        for c in side_alphabet:
            if c == side_alphabet[-1]:
                side_alphabet_to_use += c
            else:
                side_alphabet_to_use += c+"-"
        print((side_alphabet_to_use+"-"+alphabets[size-(size-(i+1))]+"-"+side_alphabet_to_use[::-1]).center((size*2-1)+(size*2-2),'-'))
            
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)