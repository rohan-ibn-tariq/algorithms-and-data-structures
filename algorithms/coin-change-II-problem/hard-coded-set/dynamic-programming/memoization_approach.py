#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Filename:    memoization_approach.py
Author:      Muhammad Rohan Ali ibn Tariq Asmat
Created on:  2025-08-05
Description: A memoization approach to the Coin Change II Problem(hard coded set).
             coins = [1, 3, 5]


Usage:
    python memoization_approach.py

Dependencies:
    - None

License: As of Repository License

Labels: Dynamic-Programming, Memoization-Approach, Coin-Change-II-Problem, Hard-Coded-Set

Time Complexity: O(n)
Space Complexity: O(n)
"""

def coin_combinations_subproblem(n: int, dp: list) -> int:
    """
    Calculate the coin combination's subproblem to account for 
    an amount n using a hard-coded set of coins, [1, 3, 5]
    through Memoization Dynamic Programming Approach.
    """
    if n < 0:
        return 0

    if dp[n] != -1:
        return dp[n]

    dp[n] = (   coin_combinations_subproblem(n - 1, dp)  # Using coin of value 1
              + coin_combinations_subproblem(n - 3, dp)  # Using coin of value 3
              + coin_combinations_subproblem(n - 5, dp)  # Using coin of value 5
            )

    return dp[n]


def coin_combinations(n: int) -> int: 
    """
    Calculate the number of combinations to account for 
    an amount n using a hard-coded set of coins, [1, 3, 5]
    through Memoization Dynamic Programming Approach.
    """

    dp = [-1] * (n + 1)
    dp[0] = 1  # Base case: one way to make amount 0
    combinations = coin_combinations_subproblem(n, dp)

    return combinations


if __name__ == "__main__":
    n = 4 # Target amount
    # Should print: 3
    print(f"All possible combinations: {coin_combinations(n)}")

    n = 6 # Target amount
    # Should print: 8
    print(f"All possible combinations: {coin_combinations(n)}")

    n = 7 # Target amount
    # Should print: 8
    print(f"All possible combinations: {coin_combinations(n)}")
