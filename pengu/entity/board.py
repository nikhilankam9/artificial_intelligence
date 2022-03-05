from common.common import Cell

class Board:
    def __init__(self, r, c) -> None:
        self.row = r
        self.col = c
        self.grid = [[Cell.empty for _ in range(c)] for _ in range(r)]

    def update(self, r, c, element):
        self.grid[r][c] = Cell(element)

    def get(self, r, c) -> Cell:
        return self.grid[r][c]

    def layout(self):
        return self.grid