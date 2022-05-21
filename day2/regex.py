# AUTHOR : MOHIT
# DATE : 2022 May 21

import re
# pattern="@gmail.com"
# print(re.search(pattern,"mohit@gmail.com"))
# res=re.search(pattern,"mohit@gmail.commohit")
# # print(resn.expand('xyz'))
# print(res)
# if res:
#     print("Valid")
# else:
#     print("InValid")



# # phone number validator:

# phNum=input()
# pattern="977"
# if re.match(pattern,phNum):
#     print(f"{phNum} : Nepal")
# else:
#     print(f"{phNum} : Not Nepali")

# search , match and findall and finditer function of re :
pattern=r"d"
match=re.match(pattern,"rich dad and poor dad")#....> returns the match object if pattern matched else returns None : checks at the begining of the given str
search=re.search(pattern,"rich dad and poor dad") #....> returns the match object if pattern matched else returns None : checks in the entire str 
finditer=re.finditer(pattern,"rich dad and poor dad") #...> returns a match iterator 
findall=re.findall(pattern,"rich dad and poor dad") #....> returns a list of matched string from given string
print(findall)
if match:
    print("Matched at the begining.")
else: 
    print("Not matched at the begining,")

if search:
    print("matched at the string.")
else:
    print("Not matched at the string.")

print("<-----------------------findall list------------------------->")
for i in findall:
    print(i)
    
print("<-----------------------finditer Iterator------------------------->")
for  i in finditer:
        print("\n")
        print(i.group())  #.>>>> returns the matched str 
        print(i.start())  # ..>>>> returs the startinf index of the matched string
        print(i.end())   #...>>>> returns the endinag index of the matched srtring
        print(i.span())  #...>>>> returns the starting and the ending index of the matched string as a tuple 


# search and replace:
_str="Hello Mohit , How are you?"
pattern=r"Mohit"
newStr=re.sub(pattern,"Elon",_str,count=1)
print(newStr)
pattern=r"How are you?"
newStr=re.sub(pattern, "I am fine.",newStr)
print(newStr)


