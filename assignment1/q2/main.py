import math
import optimization

starting_points = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
step_sizes = [0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07, 0.08, 0.09, 0.1]


def func(x):
    return math.sin((x ** 2) / 2) / math.log(x + 4, 2)

# for starting_point in starting_points:
#     print()
#     print("Starting Point: ", starting_point)
#     print()
#     for step_size in step_sizes:
#         print(optimization.hill_climb(func, starting_point, step_size))


chosen_step_sizes = [0.06, 0.07, 0.08]
temperatures = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
cooling_rates = [0.00001, 0.00002, 0.00003]

for i in range(1, 100):
    max = 0
    temp_opt = 0
    cool_opt = 0
    step_opt = 0
    for step_size in chosen_step_sizes:
        for temp in temperatures:
            for cooling_rate in cooling_rates:
                sum = 0
                for starting_point in starting_points:
                    result = optimization.simulated_annealing(func, starting_point, step_size, [0, 10], temp, cooling_rate)
                    sum += result[1]
                if sum/len(starting_points) > max:
                    max = sum/len(starting_points)
                    temp_opt = temp
                    cool_opt = cooling_rate
                    step_opt = step_size
    print(max, temp_opt, cool_opt, step_opt)
