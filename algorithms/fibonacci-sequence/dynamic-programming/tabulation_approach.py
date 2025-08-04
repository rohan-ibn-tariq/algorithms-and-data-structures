#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Filename:    tabulation_approach.py
Author:      Muhammad Rohan Ali ibn Tariq Asmat
Created on:  2025-08-04
Description: A tabulation approach to the fibonacci sequence.

Usage:
    python tabulation_approach.py

Dependencies:
    - None

License: As of Repository License

Labels: Dynamic-Programming, Fibonacci-Sequence, Tabulation-Approach
"""

def fibonacci(n: int) -> int: 
    """
    Calculate the nth Fibonacci number using a tabulation approach.
    """
    if n <= 1:
        return n

    dp = [0] * (n + 1)
    dp[0] = 0
    dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]


if __name__ == "__main__":
    n = 5
    # Should print: 5
    print(f"Fibonacci number at position {n} is: {fibonacci(n)}")

    n = 10
    # Should print: 55
    print(f"Fibonacci number at position {n} is: {fibonacci(n)}")
