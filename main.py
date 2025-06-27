from core.problem import Problem
from utils.utils import load_initial_state

print("⏳ Đang load map và sinh successors...\n")

# Khởi tạo bài toán từ file map
problem = Problem("assets/maps/map1.txt")

# Lấy state ban đầu
initial = problem.initial_state

print("🔰 Initial state:")
initial.print_board()

# Lấy các state kế tiếp
successors = problem.get_successors(initial)

print(f"\n✅ Có {len(successors)} trạng thái kế tiếp:")
for i, s in enumerate(successors):
    print(f"\n➡ Successor {i + 1}: move = {s.move}, cost = {s.cost}")
    s.print_board()