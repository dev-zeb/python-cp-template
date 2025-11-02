# Python Competitive Programming Template

A beginner-to-advanced Python template for Competitive Programming (CP), ready for contests, learning, and sharing.

## ✨ Features

- Fast I/O setup
- Common utility functions (reverse, map/filter/reduce)
- Heap / priority queue helpers (min/max)
- Binary search, sliding window, prefix sum
- Tree and graph structures with DFS/BFS
- Dynamic programming memoization decorator
- OOP starter (classes, inheritance, polymorphism)
- Multiple input helpers (single int, list, matrix, strings, graph edges)

## 📁 Repository Structure
```

python-cp-template/  
│  
├── README.md  
├── python_cp_template.py  
├── requirements.txt  
├── examples/  
│ ├── graph_examples.py  
│ ├── tree_examples.py  
│ ├── dp_examples.py  
│ ├── heap_examples.py  
│ └── input_examples.py  
└── LICENSE

```

## 🛠️ Usage

1. Clone the repository:

```bash
git clone https://github.com/dev-zeb/python-cp-template

```

2.  Import the template in your CP code:
    

```python
from python_cp_template import *

```

3.  Use **input helpers** to read different types of input:
    

```python
n = read_int()          # single integer
arr = read_list()       # space-separated integers
matrix = read_matrix(n) # matrix of n rows
lines = read_strings(3) # 3 strings
edges = read_graph_edges(m, directed=False) # graph edges

```

4.  Use **utility functions**:
    

```python
min_heap(arr)
max_heap(arr)
binary_search(arr, target)
prefix_sum(arr)
max_sum_subarray(arr, k)

```

5.  Use **graph/tree helpers**:
    

```python
g = Graph()
g.add_edge(0,1)
g.add_edge(1,2)
g.dfs(0)  # Depth-First Search
g.bfs(0)  # Breadth-First Search

root = TreeNode(1)
root.left = TreeNode(2)
preorder(root)
bfs_tree(root)

```

6.  Use **DP memoization** for recursive solutions:
    

```python
@memoize
def fib(n):
    if n <= 1: return n
    return fib(n-1) + fib(n-2)

```

7.  For **OOP practice**:
    

```python
s = Student("Alice", 20, "A")
s.greet()

```

8.  Check the `examples/` folder for full demos.
