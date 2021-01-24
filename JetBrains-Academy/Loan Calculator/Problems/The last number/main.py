"""
Given a tuple consisting of numbers, print its last element.
Sample Input:
24 22 42

Sample Output:
42
"""
print(tuple(int(n) for n in input().split())[-1])
