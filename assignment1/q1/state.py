class State:
    def __init__(self, state, cost=0, prev=None, total_cost=0):
        self.state = state
        self.cost = cost
        self.prev = prev
        self.total_cost = total_cost

    def __lt__(self, other):
        return self.total_cost < other.total_cost
