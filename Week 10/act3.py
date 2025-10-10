class Board:
    def __init__(self):
        self.grid = [[' ']*3 for _ in range(3)]

    def show(self):
        for row in self.grid:
            print('|'.join(row))
            print('-'*5)

    def place(self, r, c, symbol):
        if self.grid[r][c] == ' ':
            self.grid[r][c] = symbol
            return True
        return False

    def win(self, symbol):
        lines = self.grid + list(zip(*self.grid)) + [
            [self.grid[i][i] for i in range(3)],
            [self.grid[i][2-i] for i in range(3)]
        ]
        return any(all(cell == symbol for cell in line) for line in lines)

    def full(self):
        return all(cell != ' ' for row in self.grid for cell in row)


class Game:
    def __init__(self):
        self.board = Board()
        self.players = [('X', input("Player 1 name: ")), ('O', input("Player 2 name: "))]
        self.turn = 0

    def play(self):
        while True:
            self.board.show()
            symbol, name = self.players[self.turn]
            print(f"{name}'s turn ({symbol})")
            try:
                r = int(input("Row (0-2): "))
                c = int(input("Col (0-2): "))
                if not self.board.place(r, c, symbol):
                    print("Cell taken. Try again.")
                    continue
            except:
                print("Invalid input. Try again.")
                continue

            if self.board.win(symbol):
                self.board.show()
                print(f"{name} wins!")
                break
            if self.board.full():
                self.board.show()
                print("It's a draw!")
                break
            self.turn = 1 - self.turn


Game().play()
