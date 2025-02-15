import random

COST = {
    1: 60,
    2: 170,
    3: 510,
    4: 1530,
    5: 4400,
    6: 8800
}

VALUE = {
    0: 3,
    1: 12,
    2: 36,
    3: 108,
    4: 324,
    5: 972,
    6: 2916,
    7: 8748
}

def new_color():
    return random.randint(0, 5)

def new_stars():
    this_roll = random.random()
    if this_roll <= 0.81:
        return 1
    elif this_roll <= 0.99:
        return 2
    return 3

def free(round_state):
    if round_state['color'] == new_color():
        round_state['stars'] = min(round_state['stars'] + new_stars(), 7)
        round_state['rolls_to_guarantee'] = 3
    else:
        round_state['stars'] = max(round_state['stars'] - new_stars(), 0)
        round_state['finished'] = True

def premium(round_state):
    round_state['cost'] += COST[round_state['stars']]
    if round_state['rolls_to_guarantee'] == 1 or round_state['color'] == new_color():
        round_state['stars'] = min(round_state['stars'] + new_stars(), 7)
        round_state['rolls_to_guarantee'] = 3
    else:
        round_state['rolls_to_guarantee'] -= 1

def new_round():
    return {
        'color': new_color(),
        'stars': new_stars(),
        'cost': 60,
        'rolls_to_guarantee': 3,
        'finished': False
    }

def play_round(free_until, claim_at):
    round_state = new_round()
    if round_state['stars'] >= claim_at:
        round_state['finished'] = True
    while not round_state['finished']:
        if round_state['stars'] < free_until:
            free(round_state)
        else:
            premium(round_state)
        if round_state['stars'] >= claim_at:
            round_state['finished'] = True
    return round_state

def play_n_rounds(free_until, claim_at, n):
    total_cost = 0
    total_value = 0
    for _ in range(n):
        round_state = play_round(free_until, claim_at)
        total_cost += round_state['cost']
        total_value += VALUE[round_state['stars']]
    print(f'({free_until}, {claim_at}): {total_value / total_cost:.4f}')

if __name__ == '__main__':
    n = 10000000
    play_n_rounds(1, 1, n)
    play_n_rounds(1, 2, n)
    play_n_rounds(1, 3, n)
    play_n_rounds(1, 4, n)
    play_n_rounds(1, 5, n)
    play_n_rounds(1, 6, n)
    play_n_rounds(1, 7, n)
    play_n_rounds(2, 2, n)
    play_n_rounds(2, 3, n)
    play_n_rounds(2, 4, n)
    play_n_rounds(2, 5, n)
    play_n_rounds(2, 6, n)
    play_n_rounds(2, 7, n)
    play_n_rounds(3, 3, n)
    play_n_rounds(3, 4, n)
    play_n_rounds(3, 5, n)
    play_n_rounds(3, 6, n)
    play_n_rounds(3, 7, n)
    play_n_rounds(4, 4, n)
    play_n_rounds(4, 5, n)
    play_n_rounds(4, 6, n)
    play_n_rounds(4, 7, n)
    play_n_rounds(5, 5, n)
    play_n_rounds(5, 6, n)
    play_n_rounds(5, 7, n)
    play_n_rounds(6, 6, n)
    play_n_rounds(6, 7, n)
    play_n_rounds(7, 7, n)
