
def takeInput():
    equations = []
    # taking input manually
    # n = input("Enter Number of Variables : ")
    # no_eqn = int(input("Enter Number of Eqution : "))
    # for i in range(no_eqn):
    #     eq = input(f"Enter Eq {i+1} : ")
    #     equtions.append(eq) 

    # taking input from data file
    with open('equation.txt','r') as f:
        for i in f:
            if "\n" in i:
                i = i.replace("\n",'')
            equations.append(i)
        f.close()
    return equations

def findDeterminant(*data):
    print(f" data = {data}")
    if len(data) == 2:
        d = int(data[0][0]) * int(data[1][-1]) - (int(data[0][-1])*int(data[1][0]))
        return d
    elif len(data) == 3:
        d = (( int(data[0][0]) * int(data[1][1]) * int(data[2][2])) + ( int(data[1][0]) * int(data[2][1]) * int(data[0][2])) + ( int(data[2][0]) * int(data[0][1]) * int(data[1][2])))   -    (( int(data[0][2]) * int(data[1][1]) * int(data[2][0])) + ( int(data[1][2]) * int(data[2][1]) * int(data[0][0])) + ( int(data[2][2]) * int(data[0][1]) * int(data[1][0])))
        return d

def process(equations):
    # making matrix of coeff.s and constants
    coff_data = [[] for x in range(len(equations)+1)] # [[coff. x],[coff. y], [...],[constnts]]
    equation_data =[]
    for eq in equations:
        terms = ["" for x in range(len(equations)+1)]
        current_ind =0
        for i,c in enumerate(eq):
            if c == " ":
                continue
            if c in ("+","="):
                current_ind +=1
                continue
            if c == "-" and eq[i-1] != "=":
                current_ind += 1
                terms[current_ind] += c
            elif c == "-" and eq[i-1] == "=":
                terms[current_ind] += c
            else:
                terms[current_ind] += c
        equation_data.append(terms) 
    
    for i,eq in enumerate(equation_data):
        for j,term in enumerate(eq):
            if len(equation_data) == 3:
                if term[-1] == "x":
                    if term == "x":
                        coff_data[0].append('1')
                    elif term == "-x":
                        coff_data[0].append('-1')
                    else:
                        coff_data[0].append(term.replace("x",''))
                elif term[-1] == "y":
                    if term == "y":
                        coff_data[1].append('1')
                    elif term == "-y":
                        coff_data[1].append('-1')
                    else:
                        coff_data[1].append(term.replace("y",''))
                elif term[-1]=="z":
                    if term == "z":
                        coff_data[2].append('1')
                    elif term == "-z":
                        coff_data[2].append('-1')
                    else:
                        coff_data[2].append(term.replace("z",''))
                else:
                    coff_data[3].append(term)
            elif len(equation_data) == 2:
                if term[-1] == "x":
                    if term == "x":
                        coff_data[0].append('1')
                    elif term == "-x":
                        coff_data[0].append('-1')
                    else:
                        coff_data[0].append(term.replace("x",''))
                elif term[-1] == "y":
                    if term == "y":
                        coff_data[1].append('1')
                    elif term == "-y":
                        coff_data[1].append('-1')
                    else:
                        coff_data[1].append(term.replace("y",''))
                else:
                    coff_data[2].append(term)

    # finding determinants
    if len(equations) == 2:
        d = findDeterminant(coff_data[0],coff_data[1])
        d1 = findDeterminant(coff_data[-1],coff_data[1])
        d2 = findDeterminant(coff_data[0],coff_data[-1])
        print(f"D = {d} , D1 = {d1} , D2 = {d2} , X = {d1//d} , Y = {d2//d}")
    elif len(equations) == 3:
        d = findDeterminant(coff_data[0],coff_data[1],coff_data[2])
        d1 = findDeterminant(coff_data[-1],coff_data[1],coff_data[2])
        d2 = findDeterminant(coff_data[0],coff_data[-1],coff_data[2])
        d3 = findDeterminant(coff_data[0],coff_data[1],coff_data[-1])
        print(f"D = {d} , D1 = {d1} , D2 = {d2} , D3 = {d3} , X = {d1//d} , Y = {d2//d} , Z = {d3//d}")

if __name__ == "__main__":
    inp = takeInput()
    process(inp)