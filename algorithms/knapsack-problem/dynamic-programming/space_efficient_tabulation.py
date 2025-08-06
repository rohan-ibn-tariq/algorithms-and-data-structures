#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Filename:    space_efficient_tabulation.py
Author:      Muhammad Rohan Ali ibn Tariq Asmat
Created on:  2025-08-06
Description: A space-efficient tabular approach to the knapsack problem.

Usage:
    python space_efficient_tabulation.py

Dependencies:
    - None

License: As of Repository License

Labels: Dynamic-Programming, Knapsack-Problem, Dynamic-Set, Tabular-Approach

Time Complexity: O(n * W)
Space Complexity: O(W)
"""


def knapsack(values: list, weights: list, W: int) -> int:
    """
    Calculate the maximum value that can be obtained
    by selecting items with given values and weights
    without exceeding the maximum weight capacity W.
    """
    n = len(values)
    dp = [0] * (W + 1)

    for i in range(n):
        for w in range(W, weights[i] - 1, -1):
            dp[w] = max(dp[w], dp[w - weights[i]] + values[i])

    return dp[W]


if __name__ == "__main__":
    values = [1, 2, 3]
    weights = [4, 5, 1]
    W = 4 # Maximum weight capacity
    # Should print: 3
    print(f"Maximum Possible Value: {knapsack(values, weights, W)}")

    values  = [60, 100, 120]
    weights = [10, 20, 30]
    W = 50 # Maximum weight capacity
    # Should print: 220
    print(f"Maximum Possible Value: {knapsack(values, weights, W)}")
