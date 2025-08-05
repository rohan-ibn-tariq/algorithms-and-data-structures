#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Filename:    naive_solution.py
Author:      Muhammad Rohan Ali ibn Tariq Asmat
Created on:  2025-08-05
Description: A naive approach to the Coin Change II Problem(hard coded set).

Usage:
    python naive_solution.py

Dependencies:
    - None

License: As of Repository License

Labels: Naive-Solution, Coint-Change-II-Problem, Hard-Coded-Set

Time Complexity: O(2^n)
Space Complexity: O(n)
"""

def cutting_rod_subproblem(prices: list, n: int, dp: list) -> int: 
    """
    Calculating the subproblem for maximum obtainable price for a 
    rod of length n using a memoization approach.
    """
    if dp[n] != -1:
        return dp[n]
    
    if n == 0:
        dp[n] = 0
        return dp[n]
    
    max_price = float('-inf')
    for i in range(1, n + 1):
        if i <= len(prices):
            max_price = max(max_price, prices[i - 1] + cutting_rod_subproblem(prices, n - i, dp))
    
    dp[n] = max_price
    return dp[n]


if __name__ == "__main__":
    prices = [3, 5, 8, 9, 10]
    n = 5
    # Should print: 15
    print(f"Maximum obtainable price is: {cutting_rod(prices, n)}")

    prices.clear()
    prices = [1, 5, 8, 9, 10, 17, 17, 20]
    n = 8
    # Should print: 22
    print(f"Maximum obtainable price is: {cutting_rod(prices, n)}")
