

# ***State Formulation _ Rush Hour***

## 1. Tổng quan cấu trúc và mục đích

- `vehicle.py`: Định nghĩa đối tượng xe (Vehicle) bao gồm tên, toạ độ, hướng di chuyển, và độ dài.
- `state.py`: Định nghĩa một trạng thái trò chơi (State), lưu trữ tất cả các xe, chi phí, bước đi dẫn đến trạng thái này và trạng thái cha.
- `problem.py`: Định nghĩa bài toán Rush Hour, quản lý trạng thái ban đầu, sinh các trạng thái kế tiếp, kiểm tra mục tiêu (goal), và kiểm tra tính hợp lệ của các bước di chuyển.
- `board.py`: (Tuỳ chọn) Hiển thị bản cờ hoặc dùng cho GUI hỗ trợ.

## 2. Chi tiết từng thành phần

### 2.1 `vehicle.py`
- Lớp `Vehicle` biểu diễn một chiếc xe:
  - `name`: Tên xe, ví dụ 'X' cho xe cần giải thoát.
  - `row`, `col`: Toạ độ đầu xe (dòng, cột).
  - `direction`: 'H' (ngang) hoặc 'V' (dọc).
  - `length`: Độ dài xe (2 hoặc 3).
- Hàm `cells()`: Trả về danh sách các ô mà xe đang chiếm.

### 2.2 `state.py`
- Lớp `State` biểu diễn một trạng thái bản cờ:
  - `vehicles`: Dict các xe đang có trong trạng thái.
  - `move`: Bước đi (name, delta) dẫn đến trạng thái này.
  - `parent`: Trạng thái cha.
  - `cost`: Tổng chi phí đến hiện tại.
- Hàm `move_vehicle(name, delta)`: Di chuyển xe theo hướng chỉ định.
- Hàm `get_path()`: Truy ngược đường đi từ initial_state đến trạng thái hiện tại.
- Hàm `print_board()`: In bản cờ 6x6 ra console để debug.
- Đã hỗ trợ `__eq__` và `__hash__` để có thể dùng với set, dict.

### 2.3 `problem.py`
- Lớp `Problem` quản lý trò chơi Rush Hour:
  - Khởi tạo với đường dẫn đến file bản đồ (`map1.txt`, ...).
  - `initial_state`: Trạng thái khởi tạo.
  - `get_successors(state)`: Trả về danh sách các trạng thái hợp lệ kế tiếp, mỗi lần chỉ di chuyển đúng 1 ô.
  - `can_move(vehicle, state, delta)`: Kiểm tra xem xe có thể di chuyển 1 bước theo delta không.
  - `get_occupied_cells(state)`: Lấy danh sách tất cả các ô đang bị chiếm.
  - `is_goal(state)`: Kiểm tra xe 'X' đã đến cổng ra chưa.

## 3. Các ràng buộc đã được đảm bảo
- Chỉ di chuyển đúng 1 bước mỗi lần (delta = -1 hoặc +1).
- Xe chỉ di theo hướng của nó (ngang: trái/phải, dọc: lên/xuống).
- Không được di ra ngoài bản cờ (6x6).
- Không được đè lên xe khác hoặc nhảy qua.

## 4. Cách sử dụng `core/` trong thuật toán
Tất cả các file thuật toán (trong thư mục `search/`) chỉ cần sử dụng như sau:
```python
from core.problem import Problem
problem = Problem("maps/map1.txt")
initial_state = problem.initial_state
if problem.is_goal(state): ...
for s in problem.get_successors(state): ...
path = state.get_path()
```


```

