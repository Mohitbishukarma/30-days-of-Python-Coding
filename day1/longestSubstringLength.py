class LongestSubstringLength():
    def longestSubstringLength(self,s):     
        def subStrings(string:str):
            sbtrs=[]
            for i in range(len(string)):
                x=len(string)
                for i in range(x):
                    sbtrs.append(string[0:x])
                    x-=1
                string = string.replace(string[0],'',1)
            return  sbtrs
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

