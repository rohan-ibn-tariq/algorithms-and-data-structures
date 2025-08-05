# Coin Change II Problem (Order Matters)

## Problem Statement

Given a set of coin denominations and a target amount, find the number of different ways to make that amount using the given coins. Each coin can be used unlimited times and the order of coins matters.

## Definition

- **Coins:** Available denominations [1, 3, 5]
- **Target:** Amount n to make
- **Goal:** Count all possible ordered sequences that sum to n

## Example

**Coins:** [1, 3, 5]  
**Target:** n = 4  

**All possible ways:**
- [1,1,1,1] 
- [1,3]
- [3,1]

**Output:** 3 (total number of ways)

**Note:** [1,3] and [3,1] are counted as different ways because order matters. This is also known as "Coin Change with Permutations" or "Climbing Stairs with Variable Steps".