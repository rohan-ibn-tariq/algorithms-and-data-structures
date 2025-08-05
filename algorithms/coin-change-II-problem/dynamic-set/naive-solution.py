#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Filename:    naive_solution.py
Author:      Muhammad Rohan Ali ibn Tariq Asmat
Created on:  2025-08-05
Description: A naive approach to the Coin Change II Problem(dynamic set).

Usage:
    python naive_solution.py

Dependencies:
    - None

License: As of Repository License

Labels: Naive-Solution, Coin-Change-II-Problem, Dynamic-Set

Time Complexity: O(k^n)
Space Complexity: O(n)
"""

def coin_combinations(coins: list, n: int) -> int: 
    """
    Calculate the number of combinations to account for 
    an amount n using a dynamic set of coins.
    """

    if n < 0:
        return 0
    if n == 0:
        return 1
    
    total_combinations = 0

    for i in range(0, len(coins)):
        total_combinations += coin_combinations(coins, n - coins[i])  # Using coin of value coins[i]

    return total_combinations


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
