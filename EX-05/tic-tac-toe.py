class Board:
    def __init__(self, n=3, m=3):
        self.n = n
        self.m = m
        self.board = [['-' for _ in range(m)] for _ in range(n)]
    
    def display(self):
        for row in self.board:
            print(" | ".join(row))
    
    def check_win(self, x, y):
        """always call after move"""
        current = self.board[x][y]

        row_all_same = True
        for col in range(self.m):
            if self.board[x][col] != current:
                row_all_same = False
                break
        
        col_all_same = True
        for row in range(self.n):
            if self.board[row][y] != current:
                col_all_same = False
                break
        
        diag_all_same = True
        for row in range(self.n):
            for col in range(self.m):
                if row==col or (row+col)==(self.n-1):
                    if self.board[row][col] != current:
                        diag_all_same = False
                        break
        
        return (row_all_same or col_all_same or diag_all_same)

    def check_fill(self):
        for row in range(self.n):
            for col in range(self.m):
                if self.board[row][col] == "-":
                    return False
        return True

    def mark(self, player, x, y):
        """\
0: No win
1: X win
2: O win
3: impossible move
4: draw
"""
        if self.board[x][y] == "-":
            self.board[x][y] = player
            if self.check_win(x, y):
                if player == 'X':
                    return 1
                else:
                    return 2
            elif self.check_fill():
                return 4
            else:
                return 0
        else:
            return 3

class Marker_3x3:
    """for 3*3 board"""
    def __init__(self, board: Board, first = 'X'):
        self.board = board
        self.current = first
    
    def mark(self, pos):
        x = pos // 3
        y = pos % 3
        result = self.board.mark(self.current, x, y)

        if self.current=='X':
            self.current = 'O'
        else:
            self.current = 'X'

        return result

b = Board()

m = Marker_3x3(b)

b.display()
print(f"{m.current}'S turn.")
p = int(input("Choose a position from 1-9: ")) - 1
res = m.mark(p)

while res not in [1, 2, 4]:
    if res == 3:
        print("Invalid move. Try again.")
    b.display()
    print(f"{m.current}'S turn.")
    p = int(input("Choose a position from 1-9: ")) - 1
    res = m.mark(p)
else:
    b.display()
    if res == 1:
        print("X wins!")
    elif res == 2:
        print("O wins!")
    else:
        print("It's a draw!")
