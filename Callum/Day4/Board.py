
class Board:
    def __init__(self, rows):
        self.rows = []
        self.columns = []
        self.numbers = set()
        for rowIndex, row in enumerate(rows):
            self.rows.append(set())
            rowNumbers = row.split(' ')
            for columnIndex, number in enumerate(list(filter(None, rowNumbers))):
                self.rows[rowIndex].add(number)
                if columnIndex >= len(self.columns):
                    self.columns.append(set())
                self.columns[columnIndex].add(number)
                self.numbers.add(number)
                
    def Mark(self, number):
        self.numbers.discard(number)
        for row in self.rows:
            row.discard(number)
            if len(row) == 0:
                return True
        for column in self.columns:
            column.discard(number)
            if len(column) == 0:
                return True
            
    def Score(self):
        return sum(map(int, self.numbers))