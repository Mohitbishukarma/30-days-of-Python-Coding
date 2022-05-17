# AUTHOR : MOHIT BK
# importing required modules
import random

# required function defination:
def randomInd():
    randomLetterInd=random.randint(0,25)
    randomNumInd=random.randint(0,9)
    randomSpecialCharInd=random.randint(0,5)
    return randomLetterInd,randomSpecialCharInd,randomNumInd

def randomDataType():
    dataType=('smallLtr','num','capitalLtr','specialChar')
    randomType=random.randint(0,3)
    return dataType[randomType]

def passGen(specialChar,letters,numbers):
    randomPassLength=random.randint(8,20)
    password=''
    # print(randomPassLength)
    for i in range(randomPassLength):
        _randomDataType=randomDataType()
        (randomLetterInd,randomSpecialCharInd,randomNumInd)=randomInd()

        if _randomDataType=="smallLtr":
            password+=letters[randomLetterInd]
        elif _randomDataType=="num":
            password+=str(numbers[randomNumInd])
        elif _randomDataType=="capitalLtr":
            password+=letters[randomLetterInd].capitalize()
        else:
            password+=specialChar[randomSpecialCharInd]
    return password

def passCheck(password):
    passwordCharList=[char for char in password]
    _specialChars=0
    _capitalLtrs=0
    _numbers=0
    _smallLtrs=0
    for char in passwordCharList:
        if char in ("$","#","!","@","*","&"):
            _specialChars+=1
        elif char.isupper():
            _capitalLtrs+=1
        elif char.islower():
            _smallLtrs+=1
        else:
            _numbers+=1
    if (_specialChars>=2) and (_numbers>=2) and (_capitalLtrs>=2):
        return True
        
    else:
        return False

# required data:
specialChar= ("$","#","!","@","*","&")
letters=('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z')
numbers=(1,2,3,4,5,6,7,8,9,0)

# password validating:
if __name__=='__main__':
    password=passGen(specialChar,letters,numbers)
    while True:
        isValid=passCheck(password)
        if isValid==True:
            print(password)
            print(isValid)
            break
        else:
            print(isValid)
            password=passGen(specialChar,letters,numbers)
