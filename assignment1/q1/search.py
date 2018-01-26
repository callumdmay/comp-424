import util
import _heapq
import copy

def dfs(cur_state_obj, goal_state_obj):
    prev_states = []

    stack = []
    iterations = 0
    while not util.state_equal(cur_state_obj.state, goal_state_obj.state):
        iterations += 1
        prev_states.append(cur_state_obj)
        possible_next_states = util.get_next_states(cur_state_obj)
        new_states = list(
            filter(lambda new_state: not util.is_in_prev(new_state.state, prev_states), possible_next_states))
        sorted_new_states = sorted(new_states, key=lambda state_obj: state_obj.cost, reverse=True)

        for new_state_obj in sorted_new_states:
            new_state_obj.total_cost = cur_state_obj.total_cost + 1
            stack.append(new_state_obj)
        if stack:
            cur_state_obj = stack.pop()

    print("Total cost: ", cur_state_obj.total_cost)
    print("Iterations: ", iterations)
    util.print_path(cur_state_obj)

def bfs(cur_state_obj, goal_state_obj):
    prev_states = []
    queue = []
    iterations = 0

    while not util.state_equal(cur_state_obj.state, goal_state_obj.state):
        iterations += 1
        prev_states.append(cur_state_obj)
        possible_next_states = util.get_next_states(cur_state_obj)
        new_states = list(
            filter(lambda new_state: not util.is_in_prev(new_state.state, prev_states), possible_next_states))
        sorted_new_states = sorted(new_states, key=lambda state_obj: state_obj.cost, reverse=False)

        for new_state_obj in sorted_new_states:
            new_state_obj.total_cost = cur_state_obj.total_cost + 1
            queue.insert(0, new_state_obj)
        if queue:
            cur_state_obj = queue.pop()

    print("Total cost: ", cur_state_obj.total_cost)
    print("Iterations: ", iterations)
    util.print_path(cur_state_obj)


def uniform_cost_search(cur_state_obj, goal_state_obj):
    prev_states = []

    queue = []
    iterations = 0
    while not util.state_equal(cur_state_obj.state, goal_state_obj.state):
        iterations += 1
        prev_states.append(cur_state_obj)
        possible_next_states = util.get_next_states(cur_state_obj)
        new_states = list(
            filter(lambda new_state: not util.is_in_prev(new_state.state, prev_states), possible_next_states))
        sorted_new_states = sorted(new_states, key=lambda state_obj: state_obj.cost, reverse=False)
        for new_state_obj in sorted_new_states:
            new_state_obj.total_cost = cur_state_obj.total_cost + 1
            _heapq.heappush(queue, (new_state_obj.total_cost, new_state_obj))
        if queue:
            cur_state_obj = _heapq.heappop(queue)[1]

    print("Total cost: ", cur_state_obj.total_cost)
    print("Iterations: ", iterations)
    util.print_path(cur_state_obj)

def iterative_deepening_search(cur_state_obj, goal_state_obj, max_depth):
    initial_state_obj = copy.copy(cur_state_obj)
    iterations = 1
    for cur_depth in range(0, max_depth):
        prev_states = []
        stack = []
        cur_state_obj = initial_state_obj
        while not util.state_equal(cur_state_obj.state, goal_state_obj.state):
            iterations += 1
            prev_states.append(cur_state_obj)
            possible_next_states = util.get_next_states(cur_state_obj)
            new_states = list(
                filter(lambda new_state: not util.is_in_prev(new_state.state, prev_states), possible_next_states))
            sorted_new_states = sorted(new_states, key=lambda state_obj: state_obj.cost, reverse=True)

            for new_state_obj in sorted_new_states:
                new_state_obj.total_cost = cur_state_obj.total_cost + 1
                if new_state_obj.total_cost <= cur_depth:
                    stack.append(new_state_obj)
            if stack:
                cur_state_obj = stack.pop()
            else:
                break

        if util.state_equal(cur_state_obj.state, goal_state_obj.state):
            break

    print("Total cost: ", cur_state_obj.total_cost)
    print("Iterations: ", iterations)
    util.print_path(cur_state_obj)