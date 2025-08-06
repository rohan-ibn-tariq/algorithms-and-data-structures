#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Filename:    tabular_approach.py
Author:      Muhammad Rohan Ali ibn Tariq Asmat
Created on:  2025-08-06
Description: A tabular approach to the knapsack problem.

Usage:
    python tabular_approach.py

Dependencies:
    - None

License: As of Repository License

Labels: Dynamic-Programming, Knapsack-Problem, Dynamic-Set, Tabular-Approach

Time Complexity: O(n * W)
Space Complexity: O(n * W)
"""


def knapsack(values: list, weights: list, W: int) -> int:
    """
    Calculate the maximum value that can be obtained
    by selecting items with given values and weights
    without exceeding the maximum weight capacity W.
    """
    n = len(values)

    dp = []
    for _ in range(n + 1):
        dp.append([0] * (W + 1))

    for i in range(1, n + 1):
        for w in range(1, W+1):
            if weights[i-1] > w:
                dp[i][w] = dp[i-1][w]
            else:
                exclude_item = dp[i-1][w]
                include_item = values[i-1] + dp[i-1][w - weights[i-1]]
                dp[i][w] = max(exclude_item, include_item)

    w = W
    selected_items = []
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i-1][w]:
            selected_items.append(i-1)
            w -= weights[i-1]
    selected_items.reverse()

    return dp[n][W], selected_items


if __name__ == "__main__":
    values = [1, 2, 3]
    weights = [4, 5, 1]
    W = 4 # Maximum weight capacity
    # Should print: 3
    print(f"Maximum Possible Value, Items: {knapsack(values, weights, W)}")

    values  = [60, 100, 120]
    weights = [10, 20, 30]
    W = 50 # Maximum weight capacity
    # Should print: 220
    print(f"Maximum Possible Value, Items: {knapsack(values, weights, W)}")
