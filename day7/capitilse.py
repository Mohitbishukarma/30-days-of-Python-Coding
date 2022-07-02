# !/bin/python3.10.1
def solve(s):
    result = []
    for w in s.split(" "):
        for c in w:
            if c in "1234567890":
                result.append(w)
                break
            else:
                result.append(w.title())
                break

    return " ".join(result)
if __name__ == '__main__':

    s = input()

    result = solve(s)
    print(result)
