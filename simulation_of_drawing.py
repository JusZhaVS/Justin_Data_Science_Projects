import numpy as np
import random

def single_trial():
    prev_num = random.random()
    number_of_draws = 1
    
    while True:
        new_num = random.random()
        number_of_draws += 1
        if (new_num < prev_num):
            return number_of_draws

        prev_num = new_num

def descending_trial():
    prev_num = random.random()
    draws = 1

    while True:
        next_num = random.random()
        draws += 1
        if (next_num > prev_num):
            return draws
        prev_num = next_num

def sim_descending(n_trails = 100000):
    results = [descending_trial() for _ in range(n_trails)]
    return np.mean(results)


def simulate(n_trails = 100000):
    results = [single_trial() for _ in range(n_trails)]
    return np.mean(results)

if __name__ == "__main__":
    estimate = simulate(100000)
    print(f"Estimated expected number of draws: {estimate:.4f}")

    second_estimate = sim_descending()
    print(f"Estimated expected number of draws: {estimate:.4f}")