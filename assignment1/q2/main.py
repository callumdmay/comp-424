import math
import optimization

starting_points = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
step_sizes = [0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07, 0.08, 0.09, 0.1]


def func(x):
    return math.sin((x ** 2) / 2) / math.log(x + 4, 2)

print("Hill Climbing: ")
for starting_point in starting_points:
    print("\nStarting Point: ", starting_point, end="\n\n")
    for step_size in step_sizes:
        print(optimization.hill_climb(func, starting_point, step_size))

print("\n*****************************\n")
print("Simulated Annealing: ")
chosen_step_sizes = [0.06, 0.07, 0.08]

for starting_point in starting_points:
    print("\nStarting point: ", starting_point, end="\n\n")
    for step_size in chosen_step_sizes:
        result = optimization.simulated_annealing(func, starting_point, step_size, [0, 10], 0.7, 0.00001)
        print(result)
