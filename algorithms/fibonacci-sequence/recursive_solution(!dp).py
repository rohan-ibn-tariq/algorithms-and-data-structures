#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Filename:    recursive_solution(!dp).py
Author:      Muhammad Rohan Ali ibn Tariq Asmat
Created on:  2025-08-04
Description: A plain recursive solution to the fibonacci sequence.

Usage:
    python recursive_solution(!dp).py

Dependencies:
    - None

License: As of Repository License

Labels: Dynamic-Programming, Fibonacci-Sequence, Recursive-Approach
"""

def fibonacci(n: int) -> int: 
    """
    Calculate the nth Fibonacci number using a plain recursive approach.
    """

    if n<=1:
        return n
    
    return fibonacci(n-1) + fibonacci(n-2)


if __name__ == "__main__":
    n = 5
    # Should print: 5
    print(f"Fibonacci number at position {n} is: {fibonacci(n)}")

    n = 10
    # Should print: 55
    print(f"Fibonacci number at position {n} is: {fibonacci(n)}")
