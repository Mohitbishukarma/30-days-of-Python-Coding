# 1: Display three string “Name”, “Is”, “James” as “NameIsJames”
str1="Name"
str2="Is"
str3="James"
print(str1+str2+str3)

# 2: Arrange string characters such that lowercase letters should come first

def caseSort(text:str):
    lowerLtr=''
    upperLtr=''
    for i in text:
        if i.islower():
            lowerLtr+=i
        else:
            upperLtr+=i
    return lowerLtr+upperLtr   
string="MohitBK"
print(caseSort(string))












