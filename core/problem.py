from core.state import State
from core.vehicle import Vehicle
from utils.utils import load_initial_state
from copy import deepcopy
import utils.constants as const
# GRID_SIZE = 6
# EXIT_ROW = 2
# EXIT_COL = 5  # Vị trí cổng ra của xe đỏ

class Problem:
    def __init__(self, map_file_path):
        self.initial_state = load_initial_state(map_file_path)

    def get_successors(self, state: State):
        """Sinh các trạng thái kế tiếp từ state hiện tại"""
        successors = []

        for name, vehicle in state.vehicles.items():
            for delta in [-1, 1]:  # Thử di chuyển lùi hoặc tiến
                if self.can_move(vehicle, state, delta):
                    new_state = deepcopy(state)
                    new_state.move_vehicle(name, delta)
                    new_state.parent = state
                    new_state.move = (name, delta)
                    move_cost = new_state.vehicles[name].length
                    new_state.cost = state.cost + move_cost
                    successors.append(new_state)

        return successors

    def can_move(self, vehicle: Vehicle, state: State, delta: int):
        """Kiểm tra xe có thể di chuyển delta bước không (chỉ thử +1 hoặc -1)"""
        occupied = self.get_occupied_cells(state)

        if vehicle.direction == 'H':
            if delta == -1:
                new_col = vehicle.col - 1
                if new_col < 0 or (vehicle.row, new_col) in occupied:
                    return False
            elif delta == 1:
                new_col = vehicle.col + vehicle.length
                if new_col >= const.GRID_SIZE or (vehicle.row, new_col) in occupied:
                    return False
        elif vehicle.direction == 'V':
            if delta == -1:
                new_row = vehicle.row - 1
                if new_row < 0 or (new_row, vehicle.col) in occupied:
                    return False
            elif delta == 1:
                new_row = vehicle.row + vehicle.length
                if new_row >= const.GRID_SIZE or (new_row, vehicle.col) in occupied:
                    return False
        return True

    def get_occupied_cells(self, state: State):
        """Lấy danh sách tất cả ô đang bị chiếm (trừ xe đang xét)"""
        occupied = set()
        for v in state.vehicles.values():
            for cell in v.cells():
                occupied.add(cell)
        return occupied

    def is_goal(self, state: State):
        """Trả về True nếu xe X đến được cổng thoát"""
        x = state.vehicles.get('X')
        if x is None or x.direction != 'H':
            return False
        # Kiểm tra xem phần đuôi xe X có nằm tại cột 5 chưa
        return x.row == const.EXIT_ROW and x.col + x.length - 1 == const.EXIT_COL