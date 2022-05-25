def swap_case(s:str):
    fs=""
    for char in s:
        if char.isupper():
            fs+=char.lower()
        else:
            fs+=char.upper()
    return fs

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)