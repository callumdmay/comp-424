from state import State

def get_next_states(state_obj):
    pos = state_obj.state.index(0)
    state = state_obj.state
    if pos == 0:
        next1 = state[:]
        next1[0] = next1[1]
        next1[1] = 0
        next2 = state[:]
        next2[0] = next2[3]
        next2[3] = 0
        s1 = State(next1, state[1], state_obj)
        s2 = State(next2, state[3], state_obj)
        return [s1, s2]
    if pos == 1:
        next1 = state[:]
        next1[1] = next1[0]
        next1[0] = 0
        next2 = state[:]
        next2[1] = next2[2]
        next2[2] = 0
        next3 = state[:]
        next3[1] = next3[4]
        next3[4] = 0
        s1 = State(next1, state[0], state_obj)
        s2 = State(next2, state[2], state_obj)
        s3 = State(next3, state[4], state_obj)
        return [s1, s2, s3]
    if pos == 2:
        next1 = state[:]
        next1[2] = next1[1]
        next1[1] = 0
        next2 = state[:]
        next2[2] = next2[5]
        next2[5] = 0
        s1 = State(next1, state[1], state_obj)
        s2 = State(next2, state[5], state_obj)
        return [s1, s2]
    if pos == 3:
        next1 = state[:]
        next1[3] = next1[0]
        next1[0] = 0
        next2 = state[:]
        next2[3] = next2[4]
        next2[4] = 0
        s1 = State(next1, state[0], state_obj)
        s2 = State(next2, state[4], state_obj)
        return [s1, s2]
    if pos == 4:
        next1 = state[:]
        next1[4] = next1[1]
        next1[1] = 0
        next2 = state[:]
        next2[4] = next2[3]
        next2[3] = 0
        next3 = state[:]
        next3[4] = next3[5]
        next3[5] = 0
        s1 = State(next1, state[1], state_obj)
        s2 = State(next2, state[3], state_obj)
        s3 = State(next3, state[5], state_obj)
        return [s1, s2, s3]
    if pos == 5:
        next1 = state[:]
        next1[5] = next1[2]
        next1[2] = 0
        next2 = state[:]
        next2[5] = next2[4]
        next2[4] = 0
        s1 = State(next1, state[2], state_obj)
        s2 = State(next2, state[4], state_obj)
        return [s1, s2]


def display(state_obj):
    print(state_obj.state[:3], "Cost of step: ", state_obj.cost)
    print(state_obj.state[3:])
    print()
    # print(state_obj.state, end='')

def state_equal(state1, state2):
    for i, el in enumerate(state1):
        if el != state2[i]:
            return False

    return True


def is_in_prev(state, prev_states):
    for prev_state in prev_states:
        if state_equal(state, prev_state.state):
            return True
    return False

def print_path(state_obj, steps=0):
    if state_obj:
        if state_obj.prev:
            steps += 1
        print_path(state_obj.prev, steps)
        display(state_obj)
    else:
        print("Steps: ", steps, "\n")
