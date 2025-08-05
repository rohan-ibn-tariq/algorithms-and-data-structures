#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Filename:    memoization_approach.py
Author:      Muhammad Rohan Ali ibn Tariq Asmat
Created on:  2025-08-05
Description: A memoization approach to the Coin Change II Problem(dynamic set).

Usage:
    python memoization_approach.py

Dependencies:
    - None

License: As of Repository License

Labels: Dynamic-Programming, Memoization-Approach, Coin-Change-II-Problem, Dynamic-Set

Time Complexity: O(n * k) => n = target amount, k = number of coin denominations
Space Complexity: O(n + n) = O(2n) = O(n) => n1 for recursion stack and n2 for dp array.
"""

def coin_combinations_subproblem(coins: list, n: int, dp: list) -> int:
    """
    Calculate the coin combination's subproblem to account for 
    an amount n using a dynamic set of coins,
    through Memoization Dynamic Programming Approach.
    """
    if n < 0:
        return 0

    if dp[n] != -1:
        return dp[n]

    dp[n] = 0
    for i in range(0, len(coins)):
        dp[n] += coin_combinations_subproblem(coins, n - coins[i], dp)  # Using coin of value coins[i]

    return dp[n]


def coin_combinations(coins: list, n: int) -> int: 
    """
    Calculate the number of combinations to account for 
    an amount n using a dynamic set of coins,
    through Memoization Dynamic Programming Approach.
    """

    dp = [-1] * (n + 1)
    dp[0] = 1  # Base case: one way to make amount 0
    combinations = coin_combinations_subproblem(coins, n, dp)

    return combinations


if __name__ == "__main__":
    coins = [1, 3, 5]
    n = 4 # Target amount
    # Should print: 3
    print(f"All possible combinations: {coin_combinations(coins, n)}")

    n = 6 # Target amount
    # Should print: 8
    print(f"All possible combinations: {coin_combinations(coins, n)}")

    n = 7 # Target amount
    # Should print: 8
    print(f"All possible combinations: {coin_combinations(coins, n)}")
