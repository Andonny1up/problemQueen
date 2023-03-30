import pygame
import sys

#Variables Globales
board = []
# tamaño del tablero width heigth
WIDTH = HEIGTH = 640
#color
BLACK = (110, 110, 110)
WHITE = (255, 255, 255)

def run():
    
    #Instrucciones para resolver
    for i in range(8):
        board.append(['_'] * 8)
    position = input('introduzca la posicion de la primera reina, ejemplo "A8":').upper()
    print(position)
    if len(position) == 2:
        x = converPosition(position[0])
        y = converPosition(int(position[1]))
        board[y][x] = 'R'
    else:
        board[0][0] = 'R'
        
    set_queen(7)
    for row in board:
        print(row)
    #Instrucciones para dibujar
    pygame.init()
    window = pygame.display.set_mode((WIDTH, HEIGTH))
    pygame.display.set_caption("Tablero de ajedrez")
    draw_board(window)
    pygame.display.update()
    #Cargar imagenes y redimencionarlas
    img = pygame.image.load('img/black_queen.png')
    black_queen = pygame.transform.scale(img, (80, 80))
    img = pygame.image.load('img/white_queen.png')
    white_queen = pygame.transform.scale(img, (80, 80))
    draw_queen(window,black_queen)
    #---------------
    x_r = x * 80
    y_r = y * 80
    window.blit(white_queen, (x_r, y_r))
    #---------------
    pygame.display.update()
    # Espera a que se presione la tecla de salida
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


def converPosition(x):
    """Convierte la posicion del tablero de ajedrez en indice de lista
    ejemplo A = 0, 8 = 0"""
    match x:
        case 'A' | 8:
            new_p = 0
        case 'B' | 7:
            new_p = 1
        case 'C' | 6:
            new_p = 2
        case 'D' | 5:
            new_p = 3
        case 'E' | 4:
            new_p = 4
        case 'F' | 3:
            new_p = 5
        case 'G' | 2:
            new_p = 6
        case 'H' | 1:
            new_p = 7
        case _:
            new_p = 0
    return new_p


def free(row,col):
    """Detemina si la casilla tablero[row][col] No 
    Esta siendo amenazada por alguna reina
    Devuelve True si la casilla no esta siento amenazada
    False si esta siendo amenazada"""
    for i in range(8):
        """Busca si hay una reina a lo largo de la columna
        y la fila si hay una devuelve false"""
        if board[row][i] == 'R' or board[i][col] == 'R':
                return False
    
    """Busca reinas en la diagonal de
    izquierda a derecha"""
    if row <= col:
        c = col - row
        r = 0
    else:
        r = row - col
        c = 0
            
    while c < 8 and r < 8:
        if board[r][c] == 'R':
            return False
        r += 1
        c += 1
    
    """Busca reinas en la diagonal de
    derecha a izquierda"""    
    if row <= col:
        r = 0
        c = col + row
        if c > 7:
            r = c - 7
            c = 7
    else:
        c = 7
        r = row - (7 - col)

    while c >= 0 and r < 8:
        if board[r][c] == 'R':
            return False
        r += 1
        c -= 1

    return True


def set_queen(n):
    """ Agrega n reinas al tablero.
        @param: n El número de reinas a agregar
        @return True si se pudo agregar las reinas requeridas
    """
    if n < 1:
        return True

    for idx_row in range(8):
        for idx_col in range(8):
            if free(idx_row, idx_col):
                board[idx_row][idx_col] = 'R'
                if set_queen(n-1):
                    return True
                else:
                    board[idx_row][idx_col] = '_'

    return False

#FUNCIONES DIBUJAR
def draw_board(window):
    """Dibuja solo el tablero de ajedrez"""
    color = BLACK
    for row in range(8):
        for col in range(8):
            casilla_rect = pygame.Rect(col * 80, row * 80, 80, 80)
            if (row + col) % 2 == 0:  # Casilla blanca
                color = WHITE
            else:  # Casilla negra
                color = BLACK
            pygame.draw.rect(window,color, casilla_rect)


def draw_queen(window,black_queen):
    for row in range(8):
        for col in range(8):
            if board[row][col] == 'R':
                # Dibujar la imagen de la reina en la casilla correspondiente
                x = col * 80
                y = row * 80
                window.blit(black_queen, (x, y))


if __name__ == '__main__':
    run()