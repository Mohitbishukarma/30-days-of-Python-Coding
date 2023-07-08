def printTable(table: list):    
    colWidths = [0] * len(table)

    row_len = len(table)
    col_len = len(table[0])

    for  j in range(col_len):
        for i in range(row_len):
            length = len(table[i][j])
            if length > colWidths[i]: colWidths[i] = length

    for j in range(col_len):
        for i in range(row_len):
            col1_item = table[i][j]
            print(f"{col1_item.rjust(colWidths[i])}", end=" ")
        print()

table = [
    ["pork", "beef", "boff", "chicken"],
    ["rice","roti", "briyanii", "pulau"],
    ["corrinder", "lasun", "patato", "tomato"],
]

if __name__ == "__main__":
    printTable(table)
