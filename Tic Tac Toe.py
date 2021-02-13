import sys
def showboard(m):
    print(" ",m[0][0]," | ",m[0][1]," | ",m[0][2])
    print("_____ _____ _____")
    print(" ",m[1][0]," | ",m[1][1]," | ",m[1][2])
    print("_____ _____ _____")
    print(" ",m[2][0]," | ",m[2][1]," | ",m[2][2])

def victory(m):
    for j in range(3):
            #checking sideways
            if(m[j][0]=="x" and m[j][1]=="x" and m[0][2]=="x"):
                print("x wins!")
                sys.exit()
                return()
            elif(m[j][0]=="o" and m[j][1]=="o" and m[j][2]=="o"):
                print("o wins!")
                sys.exit()
                return() 
            #checking downwards
            elif(m[0][j]=="x" and m[1][j]=="x" and m[2][j]=="x"):
                print("x wins!")
                sys.exit()
                return()
            elif(m[0][j]=="o" and m[1][j]=="o" and m[2][j]=="o"):
                print("o wins!")
                sys.exit()
                return()
    #checking diagonals
    row=0
    col=0
    xcount=0
    ocount=0
    for i in range(3):
        if(m[row+i][col+i]=="x"):
            xcount=xcount+1
        elif(m[row+i][col+i]=="o"):
            ocount=ocount+1
    if(xcount==3):
           print("x wins!")
           sys.exit()
           return()
    if(ocount==3):
           print("o wins!")
           sys.exit()
           return()           
           
 
def takencheck(i,m):
    while():
        if(i<3):
            if(m[0][i]=="x" or "o"):
                i=input("Already taken! please give new input: ")
            else:
                break
        elif(i<6 and i>3):
            if(m[1][i-3]=="x" or "o"):
                i=input("Already taken! please give new input: ")
            else:
                break
        elif(i<9 and i>6):
            if(m[2][i-6]=="x" or "o"):
                i=input("Already taken! please give new input: ")              
            else:
                break
           
           
           
           
           
           
w=3 #this is the n of n queen
board=[[0 for x in range(w)] for y in range(w)]
print("Here is the board and its locations")
print(" ",0," | ",1," | ",2)
print("_____ _____ _____")
print(" ",3," | ",4," | ",5)
print("_____ _____ _____")
print(" ",6," | ",7," | ",8)
var="x"
for i in range(9):
    i=input("Give your input here: ")
    i=int(i)
    takencheck(i,board)
    if(i<3):
        board[0][i]=var
    elif(i<6 and i>3):
        board[1][i-3]=var
    elif(i<9 and i>6):
        board[2][i-6]=var
        
    if(var=="x"):
        var="o"
    elif(var=="o"):
        var="x"
    showboard(board)
    victory(board)
    
        
        
        
        
        