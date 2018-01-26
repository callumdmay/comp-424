import search
from state import State
cur_state = [1, 4, 2, 5, 3, 0]
goal_state = [0, 1, 2, 5, 4, 3]

cur_state_obj = State(cur_state)
goal_state_obj = State(goal_state)

search.bfs(cur_state_obj, goal_state_obj)
search.uniform_cost_search(cur_state_obj, goal_state_obj)
search.dfs(cur_state_obj, goal_state_obj)
search.iterative_deepening_search(cur_state_obj, goal_state_obj, 200)