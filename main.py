from random import randrange

def DisplayBoard(board):
#
# la función acepta un parámetro el cual contiene el estado actual del tablero
# y lo muestra en la consola
#
    print("+-------+-------+-------+")
    
    for i in range(len(board)):
        print("|       |       |       |")
        for j in range(len(board[i])):
            print("|   ", end = "")
            print(board[i][j], end = "   ")
           
        print("|") 
        print("|       |       |       |")
        print("+-------+-------+-------+")

def EnterMove(board):
#
# la función acepta el estado actual del tablero y pregunta al usuario acerca de su movimiento, 
# verifica la entrada y actualiza el tablero acorde a la decisión del usuario
#
    num = int(input('Ingresa tu movimiento: '))
    for i in range(len(board)):
        for j in range(len(board[i])):
            if num == board[i][j]:
                board[i][j] = "O"
    return board

def MakeListOfFreeFields(board):
#
# la función examina el tablero y construye una lista de todos los cuadros vacíos 
# la lista esta compuesta por tuplas, cada tupla es un par de números que indican la fila y columna
#
    return None

def VictoryFor(board, sign = ''):
#
# la función analiza el estatus del tablero para verificar si
# el jugador que utiliza las 'O's o las 'X's ha ganado el juego
#
    if board[0][0] == 'X' and board[0][1] == 'X' and board[0][2] == 'X'\
        or board[1][0] == 'X' and board[1][1] == 'X' and board[1][2] == 'X'\
            or board[2][0] == 'X' and board[2][1] == 'X' and board[2][2] == 'X'\
                or board[0][0] == 'X' and board[1][0] == 'X' and board[2][0] == 'X'\
                    or board[0][1] == 'X' and board[1][1] == 'X' and board[2][1] == 'X'\
                        or board[0][2] == 'X' and board[1][2] == 'X' and board[2][2] == 'X'\
                            or board[0][0] == 'X' and board[1][1] == 'X' and board[2][2] == 'X'\
                                or board[2][0] == 'X' and board[1][1] == 'X' and board[0][2] == 'X':
        sign = 'Computer Win'
        return sign
    elif board[0][0] == 'O' and board[0][1] == 'O' and board[0][2] == 'O'\
        or board[1][0] == 'O' and board[1][1] == 'O' and board[1][2] == 'O'\
            or board[2][0] == 'O' and board[2][1] == 'O' and board[2][2] == 'O'\
                or board[0][0] == 'O' and board[1][0] == 'O' and board[2][0] == 'O'\
                    or board[0][1] == 'O' and board[1][1] == 'O' and board[2][1] == 'O'\
                        or board[0][2] == 'O' and board[1][2] == 'O' and board[2][2] == 'O'\
                            or board[0][0] == 'O' and board[1][1] == 'O' and board[2][2] == 'O'\
                                or board[2][0] == 'O' and board[1][1] == 'O' and board[0][2] == 'O':
        sign = 'You Win'
        return sign
    else:
        return True

def DrawMove(board):
#
# la función dibuja el movimiento de la maquina y actualiza el tablero
#
    flag = True
    while flag:
        num = randrange(1, 10)
        for i in range(len(board)):
            for j in range(len(board[i])):
                if num == board[i][j]:
                    board[i][j] = "X"
                    flag = False
    
    return board


ticTacBoard = [[1, 2, 3], [4, 'X', 6], [7, 8, 9]]
DisplayBoard(ticTacBoard)

while True:
    ticTacBoard = EnterMove(ticTacBoard)
    DisplayBoard(ticTacBoard)
    ticTacBoard = DrawMove(ticTacBoard)
    DisplayBoard(ticTacBoard)
    if VictoryFor(ticTacBoard) == 'You Win':
        print('You Win!!!')
        break
    elif VictoryFor(ticTacBoard) == 'Computer Win':
        print('Computer Win')
        break