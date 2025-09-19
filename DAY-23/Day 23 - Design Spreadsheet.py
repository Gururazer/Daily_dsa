class Spreadsheet:
    def __init__(self, rows: int):
        self.grid = [[0] * 26 for _ in range(rows)]
    
    def _parse_cell(self, cell: str):
        col = ord(cell[0]) - ord('A')
        row = int(cell[1:]) - 1
        return col, row


    def setCell(self, cell: str, value: int) -> None:
        col, row = self._parse_cell(cell)
        self.grid[row][col] = value

    def resetCell(self, cell: str) -> None:
        col, row = self._parse_cell(cell)
        self.grid[row][col] = 0
        
    def getValue(self, formula: str) -> int:
        parts = formula[1:].split('+')
        val1 = self._evaluate_part(parts[0])
        val2 = self._evaluate_part(parts[1])
        return val1 + val2

    def _evaluate_part(self, part: str) -> int:
        if part.isdigit():
            return int(part)
        else:
            col, row = self._parse_cell(part)
            return self.grid[row][col]