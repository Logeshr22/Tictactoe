from os import system, name
gamestillgoing=True
gameover=False
if gamestillgoing and not gameover:
    board = ["#", "-", "-", "-","-", "-", "-", "-", "-", "-"]

    def clear():
        # for windows
        if name == 'nt':
            _ = system('cls')

            # for mac and linux(here, os.name is 'posix')
        else:
            _ = system('clear')

    def displayboard():
        print(board[1] + "|" + board[2] + "|" + board[3])
        print(board[4] + "|" + board[5] + "|" + board[6])
        print(board[7] + "|" + board[8] + "|" + board[9])




    def placemarker(board,position,marker):
        board[position]=marker

    def fullboardcheck():
        row1 = board[1] == board[2] == board[3]
        row2 = board[4] == board[5] == board[6]
        row3 = board[7] == board[8] == board[9]
        column1 = board[1] == board[4] == board[7]
        column2 = board[2] == board[5] == board[8]
        column3 = board[3] == board[6] == board[9]
        diagonal1 = board[1] == board[5] == board[9]
        diagonal2 = board[3] == board[5] == board[7]
        if (row1!="-"and row1=="X"or row2!="-"and row2=="X"or row3!="-"and row3=="X")and (row1!="-"and row1=="O"or row2!="-"and row2=="O"or row3!="-"and row3=="O"):
            print("You won!")

    def choosepositionO():
        fullboardcheck()
        print("Now turn goes to player O!\n")
        range = [1,2,3,4,5,6,7,8,9]
        position = input("Choose the position from 1-9\n")
        position=int(position)
        while position not in range:
            position=int(input("Choose the valid input.\n"))
        if board[position]=="-":
            board[position] ="O"
            mark=board[position]
            checkwinner()
        else:
            while not board[position]=="-":
                print("You can't go there!\n")
                choosepositionO()
        displayboard()
        choosepositionX()

    def choosepositionX():
        fullboardcheck()
        print("Now turn goes to player X!\n")
        range = [1,2,3,4,5,6,7,8,9]
        position = input("Choose the position from 1-9\n")
        position=int(position)
        while position not in range:
            position = int(input("Choose the valid input.\n"))
        if board[position]=="-":
            board[position] = "X"
            mark=board[position]
            checkwinner()
        else:
            while not board[position]=="-":
                print("You can't go there!\n")
                choosepositionX()
        displayboard()
        choosepositionO()


    def checkwinrow():
        row1 = board[1] == board[2] == board[3]
        row2 = board[4] == board[5] == board[6]
        row3 = board[7] == board[8] == board[9]
        if row1==row2==row3!="-" and row1==row2==row3=="X":
            print("Player X has won!\n ")
            gameover = False
        elif row1==row2==row3!="-" and row1==row2==row3=="O":
            print("Player O has won!\n ")
            gameover = False
        else:
            gamestillgoing = True
    checkwinrow()


    def checkwincolumn():
        column1 = board[1] == board[4] == board[7]
        column2 = board[2] == board[5] == board[8]
        column3 = board[3] == board[6] == board[9]
        if column1==column2==column3!="-" and column1==column2==column3=="X":
            print("Player X has won!\n")
            gameover = False
        elif column1==column2==column3!="-" and column1==column2==column3=="O":
            print("Player O has won!\n")
            gameover = False
        else:
            gamestillgoing = True
    checkwincolumn()


    def checkwindiagonal():
        diagonal1 = board[1] == board[5] == board[9]
        diagonal2 = board[3] == board[5] == board[7]

        if diagonal1==diagonal2!="-" and diagonal1==diagonal2=="X":
            print("Player X has won!\n")
            gameover = False

        elif diagonal1==diagonal2!="-" and diagonal1==diagonal2=="O":
            print("Player O has won!\n")
            gameover = False

        else:
            gamestillgoing = True


    checkwindiagonal()


    def checkwinner():
        checkwinrow()
        checkwincolumn()
        checkwindiagonal()
    checkwinner()


    def choosevalidinput():
        turn = input("Choose your turn X or O?\n")
        if turn == "X":
            choosepositionX()
        elif turn == "O":
            choosepositionO()



    def turnposition():
        displayboard()
        turn = input("Choose your turn X or O?\n")
        if turn=="X":
         choosepositionX()
        elif turn=="O":
         choosepositionO()
        else:
         while not (turn=="X"or turn=="O"):
            print("Choose a valid input")
            choosevalidinput()
    turnposition()


