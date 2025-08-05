# 0/1 Knapsack Problem

## Problem Statement

Given a knapsack with maximum weight capacity and a set of items, each with a weight and value, find the maximum total value that can be obtained by selecting items without exceeding the weight capacity.

Each item can be selected at most once (0/1 choice).

## Definition

- **Capacity:** Maximum weight the knapsack can carry
- **Items:** Each item has weight `w[i]` and value `v[i]`
- **Goal:** Maximize total value while staying within weight limit

## Example

**Knapsack capacity:** 5  
**Items:**
- Item 1: weight = 2, value = 3
- Item 2: weight = 3, value = 4  
- Item 3: weight = 4, value = 5
- Item 4: weight = 5, value = 6

**Possible combinations:**
- Take items [1,2]: weight = 2+3 = 5, value = 3+4 = 7
- Take item [4]: weight = 5, value = 6
- Take item [3]: weight = 4, value = 5

**Output:** 7 (take items 1 and 2)