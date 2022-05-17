# PROBLEM STATEMNT:Write a function named collatz() that has one parameter named number. If 
# number is even, then collatz() should print number // 2 and return this value. 
# If number is odd, then collatz() should print and return 3 * number + 1.
# Then write a program that lets the user type in an integer and that keeps 
# calling collatz() on that number until the function returns the value 1. 

def collatz(number:int):
    if number==1:
        return number
    if number%2==0:
        quotient=number//2
        return collatz(quotient)
    else:
        expressionVal=3*number+1
        return collatz(expressionVal)

x=collatz(25)
print(x)