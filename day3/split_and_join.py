
def split_and_join(line):
    _list=line.split(" ")
    _str="-".join(_list)
    return _str

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)