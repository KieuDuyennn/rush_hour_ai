class Vehicle:
    def __init__(self, name, row, col, direction, length):
        """
        name: ký tự đại diện xe (ví dụ: 'X', 'A', ...)
        row, col: tọa độ đầu của xe (ô nằm trên cùng hoặc ngoài cùng bên trái)
        direction: 'H' (ngang) hoặc 'V' (dọc)
        length: 2 hoặc 3 (car hoặc truck)
        """
        self.name = name
        self.row = row
        self.col = col
        self.direction = direction
        self.length = length

    def cells(self):
        """Trả về danh sách các ô mà xe đang chiếm (list of (row, col))"""
        occupied = []
        if self.direction == 'H':
            for i in range(self.length):
                occupied.append((self.row, self.col + i))
        elif self.direction == 'V':
            for i in range(self.length):
                occupied.append((self.row + i, self.col))
        return occupied

    def __repr__(self):
        return f"Vehicle({self.name}, ({self.row}, {self.col}), {self.direction}, {self.length})"