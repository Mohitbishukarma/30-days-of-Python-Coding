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
<<<<<<< HEAD
print(x)
=======
print(x)
>>>>>>> 355fbe98026eb984a43c1aa13bd1f0ed17667231
