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


def simulate(n_trails = 100000):
    results = [single_trial() for _ in range(n_trails)]
    return np.mean(results)

if __name__ == "__main__":
    estimate = simulate(100000)
    print(f"Estimated expected number of draws: {estimate:.4f}")