from core.problem import Problem
from algorithms.bfs_test import breadth_first_search
from gui.app import App

App()

'''
problem = Problem("assets/maps/map1.txt")

state = problem.initial_state
state.print_board()

goal_state = breadth_first_search(problem)

if goal_state:
    print("✅ Found solution!")
    print("Total moves:", len(goal_state.get_path()))
    print("Moves:", goal_state.get_path())
    print("\nFinal board:")
    goal_state.print_board()
else:
    print("❌ No solution found.")
'''
