class LongestSubstringLength():
    def longestSubstringLength(self,s):     
        def substr(string):
            subStringsCom=[]
            x=len(string)
            for i in range(x):
                subStringsCom.append(string[0:x])
                x-=1
            return subStringsCom
        def subStrings(string:str):
            allSubStr=[]
            while True:
                if len(string)==1:
                    allSubStr.append([string])
                    break
                _substrCom=substr(string)
                allSubStr.append(_substrCom)
                string=string.replace(string[0],'',1)
            return allSubStr
        def check(collection:list):
            validSbtr=[]
            for i in collection:
                for j in i:
                    currentStr=""
                    for k in j:
                        if k in currentStr:
                            break
                        else:
                            currentStr+=k
                    if currentStr==j:
                        validSbtr.append(j)
            return validSbtr

        _str=s
        if _str!="":
            sbtr=subStrings(_str)
            _validSbtr=check(sbtr)
            longestSbtrLength=0
            for item in _validSbtr:
                if len(item)>longestSbtrLength:
                    longestSbtrLength=len(item)
            return longestSbtrLength

        else:
            return 0

