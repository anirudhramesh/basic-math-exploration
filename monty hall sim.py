"""Results:
10^3 runs: {'Win': 658, 'Loss': 342}
10^4 runs: {'Win': 6589, 'Loss': 3411}
10^5 runs: {'Win': 66407, 'Loss': 33593}
10^6 runs: {'Win': 666349, 'Loss': 333651}
10^7 runs: {'Win': 6666936, 'Loss': 3333064}"""

import numpy as np
from collections import Counter
from multiprocessing import Pool

def play_game():
    door_nums = list(range(3))
    door_items = np.random.choice(['Goat', 'Goat', 'Car'], (3, ), replace=False)

    initial_choice = np.random.randint(3)
    door_nums.remove(initial_choice)
    if door_items[door_nums[0]] == 'Car':
        presenter_reveals = door_nums[1]
    else:
        presenter_reveals = door_nums[0]

    door_nums.remove(presenter_reveals)
    door_nums = door_nums[0]
    if door_items[door_nums] == 'Car':
        return 'Win'
    else:
        return 'Loss'


def run_simulation(trials):
    results = []
    for _ in range(trials):
        results.append(play_game())
    return results


def parallelize_simulations():
    total_trials = 10**9
    split = [10**4] * (10**4)

    proc_pool = Pool(processes=10, maxtasksperchild=10)
    sim_split_runs = proc_pool.map(run_simulation, split)
    proc_pool.close(), proc_pool.join()

    results = []
    for sim in sim_split_runs:
        results.extend(sim)

    print(Counter(results))


if __name__ == '__main__':
    parallelize_simulations()
