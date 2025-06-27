from collections import deque

def breadth_first_search(problem):
    """
    Hàm giải bài toán Rush Hour bằng thuật toán Breadth-First Search (BFS).
    Trả về: state đích nếu tìm thấy, hoặc None nếu thất bại.
    """

    node = problem.initial_state  # node ← a node with state = initial
    if problem.is_goal(node):     # if goal-test(node.state)
        return node               # return solution

    frontier = deque()            # FIFO queue
    frontier.append(node)

    explored = set()              # explored ← an empty set

    while frontier:
        node = frontier.popleft()  # pop the shallowest node
        explored.add(node)         # add state to explored

        for child in problem.get_successors(node):  # for each action
            if child not in explored and child not in frontier:
                if problem.is_goal(child):          # if goal-test
                    return child
                frontier.append(child)

    return None  # if EMPTY?(frontier) then return failure