from core.vehicle import Vehicle
from copy import deepcopy

class State:
    def __init__(self, vehicles: dict, move=None, parent=None, cost=0):
        """
        vehicles: dict[name] = Vehicle
        move: (name, delta) → bước đi dẫn đến trạng thái này
        parent: State cha để truy ngược lời giải
        cost: tổng chi phí (dùng cho UCS, A*)
        """
        self.vehicles = vehicles
        self.move = move
        self.parent = parent
        self.cost = cost

    def __eq__(self, other):
        if not isinstance(other, State):
            return False
        return self._key() == other._key()

    def __hash__(self):
        return hash(self._key())

    def _key(self):
        """Trả về khóa đại diện cho trạng thái này (vị trí các xe)"""
        return tuple(sorted((name, v.row, v.col) for name, v in self.vehicles.items()))

    def copy(self):
        """Tạo bản sao hoàn toàn mới của state (để không làm hỏng state cũ)"""
        new_vehicles = {
            name: Vehicle(v.name, v.row, v.col, v.direction, v.length)
            for name, v in self.vehicles.items()
        }
        return State(new_vehicles, self.move, self.parent, self.cost)

    def move_vehicle(self, name, delta):
        """Di chuyển 1 xe trong vehicles"""
        v = self.vehicles[name]
        if v.direction == 'H':
            v.col += delta
        elif v.direction == 'V':
            v.row += delta

    def get_path(self):
        """Truy ngược lại từ trạng thái này về initial_state để lấy toàn bộ lời giải"""
        path = []
        state = self
        while state.parent is not None:
            path.append(state.move)
            state = state.parent
        path.reverse()
        return path

    def print_board(self):
        """In ra bàn cờ dạng 6x6 cho dễ debug"""
        board = [['.' for _ in range(6)] for _ in range(6)]
        for v in self.vehicles.values():
            for (r, c) in v.cells():
                board[r][c] = v.name
        for row in board:
            print(' '.join(row))