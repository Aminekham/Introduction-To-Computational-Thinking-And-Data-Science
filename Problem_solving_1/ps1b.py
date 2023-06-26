###########################
# 6.0002 Problem Set 1b: Space Change
# Name:Mohammed Amine Khammassi
# Collaborators:None
# Time:26/06/2023
# Author: charz, cdenise

#================================
# Part B: Golden Eggs
#================================
import time
# Problem 1
def dp_make_weight(egg_weights, target_weight, memo = {}):
    """
    Find number of eggs to bring back, using the smallest number of eggs. Assumes there is
    an infinite supply of eggs of each weight, and there is always a egg of value 1.
    
    Parameters:
    egg_weights - tuple of integers, available egg weights sorted from smallest to largest value (1 = d1 < d2 < ... < dk)
    target_weight - int, amount of weight we want to find eggs to fit
    memo - dictionary, OPTIONAL parameter for memoization (you may not need to use this parameter depending on your implementation)
    
    Returns: int, smallest number of eggs needed to make target weight
    """
    # My code :
    # Simplest solution without using dynamic programming:
    """list_of_numbers_to_use = []
    n = target_weight
    for i in range(1, len(egg_weights) + 1):
        list_of_numbers_to_use.append(n // egg_weights[-i])
        n = n % egg_weights[-i]
        print(egg_weights[-i])
    egg_number = sum(list_of_numbers_to_use)
    return(egg_number)"""
    # Solution using dynamic programming :
    start = time.time()
    dp = [float('inf')] * (target_weight + 1)
    dp[0] = 0  # Base case: 0 eggs needed to make weight 0
    for weight in range(1, target_weight + 1):
        for egg_weight in egg_weights:
            if egg_weight <= weight:
                dp[weight] = min(dp[weight], dp[weight - egg_weight] + 1)
    end = time.time()
    print("time needed for the dynamic programming algorithm: {}".format(end - start))
    print(dp)
    return dp[target_weight]

# EXAMPLE TESTING CODE, feel free to add more if you'd like
if __name__ == '__main__':
    egg_weights = (1, 5, 10, 25)
    n = 99
    print("Egg weights = (1, 5, 10, 25)")
    print("n = 99")
    print("Expected ouput: 9 (3 * 25 + 2 * 10 + 4 * 1 = 99)")
    print("Actual output:", dp_make_weight(egg_weights, n))
    print()
