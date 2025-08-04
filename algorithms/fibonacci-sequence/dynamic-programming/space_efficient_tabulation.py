#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Filename:    space_efficient_tabulation.py
Author:      Muhammad Rohan Ali ibn Tariq Asmat
Created on:  2025-08-04
Description: A space-efficient dynamic programming approach to the fibonacci sequence.

Usage:
    python space_efficient_tabulation.py

Dependencies:
    - None

License: As of Repository License

Labels: Dynamic-Programming, Fibonacci-Sequence, Space-Efficient-Tabulation
"""

def fibonacci(n: int) -> int: 
    """
    Calculate the nth Fibonacci number using space efficient tabulation approach.
    """
    current = 0
    previous = 1
    previous_previous = 0

    if n == 0:
        return previous_previous
    elif n == 1:
        return previous

    for i in range(2, n + 1):
        current = previous + previous_previous
        previous_previous = previous
        previous = current

    return current


if __name__ == "__main__":
    n = 5
    # Should print: 5
    print(f"Fibonacci number at position {n} is: {fibonacci(n)}")

    n = 10
    # Should print: 55
    print(f"Fibonacci number at position {n} is: {fibonacci(n)}")
