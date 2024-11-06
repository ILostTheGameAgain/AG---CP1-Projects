#Alec George Proficiency Test: Multiplication Table

#will print a large table of all numbers
#layout:
#   | 1 | 2 | 3 | 4 | 5 | 6 |...
#---+---+---+---+---+---+---+---
# 1 |   |   |   |   |   |   |   
#---+---+---+---+---+---+---+---
# 2 |   |   |   |   |   |   |   
#---+---+---+---+---+---+---+---
# 3 |   |   |   |   |   |   |   
#---+---+---+---+---+---+---+---
# 4 |   |   |   |   |   |   |   
#---+---+---+---+---+---+---+---
#...|   |   |   |   |   |   |   

#needs variables and user input for starting and ending amounts of rows, can't be larger than 30 because graph breaks with larger than 3 digit numbers, and a variable for the final graph
row_min = int(input("What is the lowest row number? (type an integer, 0 to 100, larger numbers can break this): "))
row_max = int(input("What is the highest row number? (type an integer, 0 to 100): "))
column_min = int(input("What is the lowest column number? (type an integer, 0 to 100): "))
column_max = int(input("What is the highest column number? (type an integer, 0 to 100): "))
graph = "     |"

#for loop to write out top row
for x in range(row_min, row_max):
    if len(str(x)) == 1:
        graph += "  "+str(x)+"  |"
    elif len(str(x)) == 2:
        graph += "  "+str(x)+" |"
    elif len(str(x)) == 3:
        graph += " "+str(x)+" |"
    elif len(str(x)) == 4:
        graph += " "+str(x)+"|"
    elif len(str(x)) == 5:
        graph += str(x)+"|"
#add last number to the list differently so no line at end
graph += " "+str(row_max)
#variable for line that spaces rows, for loop to get right length
line = ""
for x in range(row_min, row_max+1):
    line += "-----+"
line += "-----"
graph += "\n"+line

#graph the rest of the stuff on the graph
for x in range(column_min, column_max+1):
    #first display the column number
    if len(str(x)) == 1:
        graph += "\n  "+str(x)+"  |"
    elif len(str(x)) == 2:
        graph += "\n  "+str(x)+" |"
    elif len(str(x)) == 3:
        graph += "\n "+str(x)+" |"
    elif len(str(x)) == 4:
        graph += "\n "+str(x)+"|"
    elif len(str(x)) == 5:
        graph += "\n"+str(x)+"|"
    #multiply the numbers together
    for y in range(row_min, row_max+1):
        if not y == row_max:
            if len(str(x*y)) == 1:
                graph += "  "+str(x*y)+"  |"
            elif len(str(x*y)) == 2:
                graph += "  "+str(x*y)+" |"
            elif len(str(x*y)) == 3:
                graph += " "+str(x*y)+" |"
            elif len(str(x*y)) == 4:
                graph += " "+str(x*y)+"|"
            elif len(str(x*y)) == 5:
                graph += str(x*y)+"|"
        else:
            if len(str(x*y)) == 1:
                graph += "  "+str(x*y)+"  "
            elif len(str(x*y)) == 2:
                graph += "  "+str(x*y)+" "
            elif len(str(x*y)) == 3:
                graph += " "+str(x*y)+" "
            elif len(str(x*y)) == 4:
                graph += " "+str(x*y)
            elif len(str(x*y)) == 5:
                graph += str(x*y)
    #add lines to space out graph
    #don't add one for the last line
    if not x == column_max:
        graph += "\n"+line
#print the final product
print(graph)