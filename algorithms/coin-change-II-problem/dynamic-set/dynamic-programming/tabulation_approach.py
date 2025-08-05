#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Filename:    tabulation_approach.py
Author:      Muhammad Rohan Ali ibn Tariq Asmat
Created on:  2025-08-05
Description: A tabulation approach to the Coin Change II Problem(hard coded set).
             coins = [1, 3, 5]


Usage:
    python tabulation_approach.py

Dependencies:
    - None

License: As of Repository License

Labels: Dynamic-Programming, Tabulation-Approach, Coin-Change-II-Problem, Hard-Coded-Set

Time Complexity: O(n)
Space Complexity: O(n)
"""

def coin_combinations(n: int) -> int: 
    """
    Calculate the number of combinations to account for 
    an amount n using a hard-coded set of coins, [1, 3, 5]
    through Tabulation Dynamic Programming Approach.
    """
    if n < 0:
        raise ValueError("Input amount 'n' must be a non-negative integer")

    dp = [0] * (n + 1)
    dp[0] = 1  # Base case: one way to make amount 0

    for i in range(1, n + 1):
        if i - 1 >= 0:
            dp[i] += dp[i - 1]  # Using coin of value 1
        if i - 3 >= 0:
            dp[i] += dp[i - 3]  # Using coin of value 3
        if i - 5 >= 0:
            dp[i] += dp[i - 5]  # Using coin of value 5

    return dp[n]


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
