if __name__ == '__main__':
    N = int(input())
    arr=[]
    for i in range(N):
        cmd=input().split(" ")
        if "insert" in cmd:
            arr.insert(int(cmd[-2]),int(cmd[-1]))
        elif cmd[0]=="print":
            print(arr)
        elif "remove" in cmd:
            arr.remove(int(cmd[-1]))
        elif "append" in cmd:
            arr.append(int(cmd[-1]))
        elif cmd[0]=="sort":
            arr.sort()
        elif cmd[0]=="pop":
            arr.pop()
        elif cmd[0]=="reverse":
            arr.reverse()
            