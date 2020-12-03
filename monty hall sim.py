"""Results:
10^3 runs: {'Win': 658, 'Loss': 342}
10^4 runs: {'Win': 6589, 'Loss': 3411}
10^5 runs: {'Win': 66407, 'Loss': 33593}
10^6 runs: {'Win': 666349, 'Loss': 333651}"""

import numpy as np
from collections import Counter

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


def run_simulation():
    total_trials = 10**6

    results = []
    for _ in range(total_trials):
        results.append(play_game())

    print(Counter(results))


if __name__ == '__main__':
    run_simulation()
