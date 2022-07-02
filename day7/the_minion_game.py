# !/bin/python3.10.1
def minion_game(string):
    kevin_score = 0
    stuart_score = 0
    sbtrs = []
    for i in range(len(string)):
        x=len(string)
        for i in range(x):
            sbtrs.append(string[0:x])
            x-=1
        string = string.replace(string[0],'',1)
    
    for sbtr in sbtrs:
        if sbtr.startswith("A") or sbtr.startswith("E") or sbtr.startswith("I") or sbtr.startswith("O") or sbtr.startswith("U"):
            kevin_score +=1
        else:
            stuart_score += 1
    
    if kevin_score>stuart_score:
        return f"Kevin {kevin_score}"
    elif kevin_score<stuart_score:
        return f"Stuart {stuart_score}"
    else:
        return "Draw"
        

if __name__ == '__main__':
    s = input()
    result = minion_game(s)
    print(result)

