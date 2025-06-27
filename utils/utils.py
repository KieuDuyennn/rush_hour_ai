from core.vehicle import Vehicle
from core.state import State
import os

def load_initial_state(file_path):
    """
    Đọc file map.txt, tạo danh sách các Vehicle, 
    rồi trả về State ban đầu chứa các xe này.
    """
    vehicles = {}

    with open(file_path, 'r') as f:
        for line in f:
            # Ví dụ dòng: X 2 0 H 2
            parts = line.strip().split()
            if len(parts) != 5:
                continue  # bỏ qua dòng lỗi

            name, row, col, direction, length = parts
            row = int(row)
            col = int(col)
            length = int(length)

            vehicle = Vehicle(name, row, col, direction, length)
            vehicles[name] = vehicle

    # Tạo đối tượng State ban đầu
    return State(vehicles)

def get_map_files():
    folder = "assets/maps"
    return [f for f in os.listdir(folder) if f.endswith(".txt")]