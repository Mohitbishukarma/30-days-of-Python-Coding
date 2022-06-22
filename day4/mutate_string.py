"""
    python: 3.10.1
    coder: Mohit Bk
"""
def mutate_string(string, position, character):
    """ String Mutation 
    Arguments:
        string: a string
        position: a integer
        character: a character
    Returns:
        The Modified String
    """
    charList=list(string)
    charList[position]=character
    modifiedStr="".join(charList)
    return modifiedStr

if __name__ == '__main__':
    s = input()
    i, c = input().split(' ')
    s_new = mutate_string(s, int(i), c)
    print(s_new)