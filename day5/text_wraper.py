"""
    python: 3.10.1
    coder: Mohit Bk
"""

import textwrap
def wrap(string, max_width):
    ''' wrap string into max_width
    params:
        string: a string
        max_width: an integer
    returns:
        wraped string 
    '''
    wraped = textwrap.fill(string,max_width)
    return wraped

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
