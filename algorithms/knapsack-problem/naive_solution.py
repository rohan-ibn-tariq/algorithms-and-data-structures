#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Filename:    naive_solution.py
Author:      Muhammad Rohan Ali ibn Tariq Asmat
Created on:  2025-08-06
Description: A naive approach to the knapsack problem.

Usage:
    python naive_solution.py

Dependencies:
    - None

License: As of Repository License

Labels: Naive-Solution, Knapsack-Problem, Dynamic-Set

Time Complexity: O(2^n)
Space Complexity: O(n)
"""

def knapsack(i: int, values: list, weights: list, W: int) -> int: 
    """
    Calculate the maximum value that can be obtained
    by selecting items with given values and weights
    without exceeding the maximum weight capacity W.
    """
    if i >= len(values) or W <= 0:
        return 0
    
    # If the weight of the current item exceeds the capacity, skip it
    if weights[i] > W:
        return knapsack(i + 1, values, weights, W)
    
    # Otherwise, consider two cases: including or excluding the current item
    include_item = values[i] + knapsack(i + 1, values, weights, W - weights[i])
    exclude_item = knapsack(i + 1, values, weights, W)

    return max(include_item, exclude_item)


if __name__ == "__main__":
    values = [1, 2, 3]
    weights = [4, 5, 1]
    W = 4 # Maximum weight capacity
    # Should print: 3
    print(f"Maximum Possible Value: {knapsack(0, values, weights, W)}")

    values  = [60, 100, 120]
    weights = [10, 20, 30]
    W = 50
    # Should print: 220
    print(f"Maximum Possible Value: {knapsack(0, values, weights, W)}")
