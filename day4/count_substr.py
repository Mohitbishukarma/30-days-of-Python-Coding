"""
    python: 3.10.1
    coder: Mohit Bk
"""
def count_substring(string, sub_string):
    """Count apearence of sub string in string
    Parameters:
        string: a string
        sub_string: a string
    Return: 
        number of repeatation of a sub string: an integer 
    """
    sbtrs=[]
    for i in range(len(string)):
        x=len(string)
        for i in range(x):
            sbtrs.append(string[0:x])
            x-=1
        string = string.replace(string[0],'',1)
    return sbtrs.count(sub_string)



if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)