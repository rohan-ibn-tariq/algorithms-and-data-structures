#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Filename:    naive_solution.py
Author:      Muhammad Rohan Ali ibn Tariq Asmat
Created on:  2025-08-05
Description: A naive approach to the Coin Change II Problem(hard coded set).
             coins = [1, 3, 5]


Usage:
    python naive_solution.py

Dependencies:
    - None

License: As of Repository License

Labels: Naive-Solution, Coint-Change-II-Problem, Hard-Coded-Set

Time Complexity: O(3^n)
Space Complexity: O(n)
"""

def coin_combinations(n: int) -> int: 
    """
    Calculate the number of combinations to account for 
    an amount n using a hard-coded set of coins, [1, 3, 5].
    """

    if n < 0:
        return 0
    if n == 0:
        return 1
    
    total_combinations = 0
    total_combinations += coin_combinations(n - 1)  # Using coin of value 1
    total_combinations += coin_combinations(n - 3)  # Using coin of value 3
    total_combinations += coin_combinations(n - 5)  # Using coin of value 5

    return total_combinations


if __name__ == "__main__":
    n = 4 # Target amount
    # Should print: 3
    print(f"All possible combinations: {coin_combinations(n)}")

    n = 6 # Target amount
    # Should print: 8
    print(f"All possible combinations: {coin_combinations(n)}")
