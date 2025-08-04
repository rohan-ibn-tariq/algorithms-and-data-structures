#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Filename:    memoization_approach.py
Author:      Muhammad Rohan Ali ibn Tariq Asmat
Created on:  2025-08-04
Description: A memoization approach to the fibonacci sequence.

Usage:
    python memoization_approach.py

Dependencies:
    - None

License: As of Repository License
"""

def fibonacci(n: int, memo: list) -> int: 
    """
    Calculate the nth Fibonacci number using a memoization approach.
    """

    if memo[n] != -1:
        return memo[n]

    if n <= 1:
        memo[n] = n
        return memo[n]
    else:
        memo[n] = fibonacci(n-1, memo) + fibonacci(n-2, memo)

    return memo[n]


if __name__ == "__main__":
    n = 5
    memo = [-1] * (n+1)
    # Should print: 5
    print(f"Fibonacci number at position {n} is: {fibonacci(n, memo)}")

    memo.clear()
    n = 10
    memo = [-1] * (n+1)
    # Should print: 55
    print(f"Fibonacci number at position {n} is: {fibonacci(n, memo)}")
