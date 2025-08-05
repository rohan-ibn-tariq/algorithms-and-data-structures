#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Filename:    tabulation_approach.py
Author:      Muhammad Rohan Ali ibn Tariq Asmat
Created on:  2025-08-05
Description: A tabulation approach to the Cutting Rod Problem.

Usage:
    python tabulation_approach.py

Dependencies:
    - None

License: As of Repository License

Labels: Dynamic-Programming, Cutting-Rod-Problem, Tabulation-Approach

Time Complexity: O(n^2)
Space Complexity: O(n)
"""

def cutting_rod(prices: list) -> int: 
    """
    Calculating the maximum obtainable price for a 
    rod of length n using a tabulation approach.
    """
    if not prices or not all(isinstance(p, (int, float)) and p >= 0 for p in prices):
        raise ValueError("Prices must be a non-empty list of non-negative numbers.")

    n = len(prices)
    dp = [0] * (n + 1)

    for i in range(1, n + 1):
        for j in range(1, i + 1):
            dp[i] = max(dp[i], prices[j - 1] + dp[i - j])

    return dp[n]


if __name__ == "__main__":
    prices = [3, 5, 8, 9, 10]
    # Should print: 15
    print(f"Maximum obtainable price is: {cutting_rod(prices)}")

    prices.clear()
    prices = [1, 5, 8, 9, 10, 17, 17, 20]
    # Should print: 22
    print(f"Maximum obtainable price is: {cutting_rod(prices)}")

    # prices.clear()
    # # Should print: Error
    # print(f"Maximum obtainable price is: {cutting_rod(prices)}")
