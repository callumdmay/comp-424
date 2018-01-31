import random
import math

def hill_climb(func, initial_pos, step_size):
    current_pos_val = func(initial_pos)
    current_pos = initial_pos
    iterations = 0
    while True:

        temp_val = current_pos_val
        temp_pos = current_pos

        if func(current_pos + step_size) > temp_val and current_pos + step_size < 10:
            temp_val = func(current_pos + step_size)
            temp_pos = current_pos + step_size

        if func(current_pos - step_size) > temp_val and current_pos - step_size > 0:
            temp_val = func(current_pos - step_size)
            temp_pos = current_pos - step_size

        if temp_val <= current_pos_val:
            return round(current_pos, 5), round(current_pos_val, 5), iterations
        else:
            current_pos_val = temp_val
            current_pos = temp_pos
        iterations += 1


def simulated_annealing(func, initial_pos, step_size, bounded_range, temp, cooling_rate):
    current_pos = initial_pos
    current_pos_val = func(initial_pos)
    iterations = 0

    while temp > 0.00001:
        neighbours = [(func(current_pos + step_size), current_pos + step_size),
                      (func(current_pos - step_size), current_pos - step_size)]
        random_neighbour = random.choice(neighbours)

        if random_neighbour[1] < bounded_range[0] or random_neighbour[1] > bounded_range[1]:
            continue

        if random_neighbour[0] > current_pos_val:
            current_pos_val = random_neighbour[0]
            current_pos = random_neighbour[1]
        elif math.exp(-(current_pos_val - random_neighbour[0]) / temp) > random.random():
            current_pos_val = random_neighbour[0]
            current_pos = random_neighbour[1]

        temp *= cooling_rate
        iterations += 1

    return round(current_pos, 5), round(current_pos_val, 5), iterations
