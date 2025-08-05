#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Filename:    tabulation_approach.py
Author:      Muhammad Rohan Ali ibn Tariq Asmat
Created on:  2025-08-05
Description: A tabulation approach to the Coin Change II Problem(dynamic set).

Usage:
    python tabulation_approach.py

Dependencies:
    - None

License: As of Repository License

Labels: Dynamic-Programming, Tabulation-Approach, Coin-Change-II-Problem, Dynamic-Set

Time Complexity: O(n * k) => n = target amount, k = number of coin denominations
Space Complexity: O(n)
"""

def coin_combinations(coins: list, n: int) -> int: 
    """
    Calculate the number of combinations to account for 
    an amount n using a dynamic set of coins,
    through Tabulation Dynamic Programming Approach.
    """
    if n < 0:
        raise ValueError("Input amount 'n' must be a non-negative integer")

    dp = [0] * (n + 1)
    dp[0] = 1  # Base case: one way to make amount 0

    for i in range(1, n + 1):
        for coin in coins:
            if i - coin >= 0:
                dp[i] += dp[i - coin]  # Using coin of value coin

    return dp[n]


if __name__ == "__main__":
    coins = [1, 3, 5]
    n = 4 # Target amount
    # Should print: 3
    print(f"All possible combinations: {coin_combinations(coins, n)}")

    n = 6 # Target amount
    # Should print: 8
    print(f"All possible combinations: {coin_combinations(coins, n)}")

    n = 7 # Target amount
    # Should print: 12
    print(f"All possible combinations: {coin_combinations(coins, n)}")
