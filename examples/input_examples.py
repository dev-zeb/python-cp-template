# Examples showing usage of input helpers from python_cp_template.py
from python_cp_template import *

# Single integer
print("Enter a single integer:")
n = read_int()
print("You entered:", n)

# List of integers
print("\nEnter a list of integers:")
arr = read_list()
print("List:", arr)

# Matrix
print("\nEnter number of rows for matrix:")
rows = read_int()
print(f"Enter {rows} rows:")
matrix = read_matrix(rows)
print("Matrix:")
for row in matrix:
    print(row)

# Multiple strings
print("\nEnter 3 strings:")
strings = read_strings(3)
print("Strings:", strings)

# Graph edges
print("\nEnter number of edges:")
m = read_int()
print(f"Enter {m} edges (u v):")
adj = read_graph_edges(m, directed=False)
print("Adjacency list of graph:")
for u in adj:
    print(u, "->", adj[u])
