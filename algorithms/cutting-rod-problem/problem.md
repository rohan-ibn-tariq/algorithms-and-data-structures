# Rod Cutting Problem

## Problem Statement

Given a rod of length n and a list of prices for different rod lengths, find the maximum profit obtainable by cutting the rod and selling the pieces.

## Definition

You can cut the rod into any combination of smaller pieces. Each piece of length i has a price `price[i-1]`.

## Example

**Rod length:** 4  
**Prices:** [1, 5, 8, 9]  
- Length 1 rod costs $1
- Length 2 rod costs $5  
- Length 3 rod costs $8
- Length 4 rod costs $9

**Possible cuts:**
- No cuts: [4] → $9
- Cut into [2,2] → $5 + $5 = $10
- Cut into [1,3] → $1 + $8 = $9
- Cut into [1,1,1,1] → $1 + $1 + $1 + $1 = $4

**Output:** 10 (cut into two pieces of length 2)