#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Filename:    memoization_approach.py
Author:      Muhammad Rohan Ali ibn Tariq Asmat
Created on:  2025-08-06
Description: A memoization approach to the knapsack problem.

Usage:
    python memoization_approach.py

Dependencies:
    - None

License: As of Repository License

Labels: Dynamic-Programming, Knapsack-Problem, Dynamic-Set, Memoization-Approach

Time Complexity: O(n * W)
Space Complexity: O(n * W)
"""

def knapsack_subproblem(i: int, values: list, weights: list, W: int, memo: list) -> int: 
    """
    Resolving the subproblem for calculating the maximum 
    value that can be obtained
    by selecting items with given values and weights
    without exceeding the maximum weight capacity W.
    """
    if i >= len(values) or W <= 0:
        return 0
    
    if memo[i][W] != -1:
        return memo[i][W]
    
    # If the weight of the current item exceeds the capacity, skip it
    if weights[i] > W:
        memo[i][W] = knapsack_subproblem(i + 1, values, weights, W, memo)
        return memo[i][W]
    
    # Otherwise, consider two cases: including or excluding the current item
    include_item = values[i] + knapsack_subproblem(i + 1, values, weights, W - weights[i], memo)
    exclude_item = knapsack_subproblem(i + 1, values, weights, W, memo)

    result = max(include_item, exclude_item)
    memo[i][W] = result

    return result


def knapsack(values: list, weights: list, W: int) -> int:
    """
    Calculate the maximum value that can be obtained
    by selecting items with given values and weights
    without exceeding the maximum weight capacity W.
    """
    memo = []
    for _ in range(len(values)):
        memo.append([-1] * (W + 1))

    return knapsack_subproblem(0, values, weights, W, memo)


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
