# =========================================
# Python Competitive Programming Template
# Author: Sufi Aurangzeb Hossain
# GitHub: https://github.com/dev-zeb
# =========================================

# ---------- FAST I/O ----------
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

# ---------- INPUT HELPERS ----------

def read_int():
    """Read a single integer"""
    return int(input())

def read_list():
    """Read a single line of space-separated integers as a list"""
    return list(map(int, input().split()))

def read_matrix(n):
    """Read a matrix of n rows, each row space-separated"""
    return [list(map(int, input().split())) for _ in range(n)]

def read_strings(n=1):
    """Read n lines of strings"""
    if n == 1:
        return input().strip()
    return [input().strip() for _ in range(n)]

def read_graph_edges(m, directed=True):
    """
    Read m edges and return adjacency list as a dict
    directed=True for directed graph, False for undirected
    """
    g = defaultdict(list)
    for _ in range(m):
        u,v = map(int, input().split())
        g[u].append(v)
        if not directed:
            g[v].append(u)
    return g


# ---------- COMMON UTILITIES ----------
from functools import reduce
from collections import deque, defaultdict

# --- List / Array ---
def reverse_list(arr):
    """Return reversed list"""
    return arr[::-1]

def square_list(arr):
    """Return a new list with elements squared"""
    return list(map(lambda x: x*x, arr))

def filter_even(arr):
    """Return only even numbers from the list"""
    return list(filter(lambda x: x%2==0, arr))

def sum_list(arr):
    """Return sum of elements using reduce"""
    return reduce(lambda acc,x: acc+x, arr)

def prefix_sum(arr):
    """Return prefix sum array"""
    ps = [0]*(len(arr)+1)
    for i in range(len(arr)):
        ps[i+1] = ps[i] + arr[i]
    return ps

def max_sum_subarray(arr, k):
    """Return maximum sum of subarray of size k"""
    n = len(arr)
    if n < k: return None
    curr_sum = sum(arr[:k])
    max_sum = curr_sum
    for i in range(k, n):
        curr_sum += arr[i] - arr[i-k]
        max_sum = max(max_sum, curr_sum)
    return max_sum

# ---------- HEAP (PRIORITY QUEUE) ----------
import heapq

def min_heap(arr):
    """Return sorted list using min-heap"""
    pq = []
    for x in arr: heapq.heappush(pq, x)
    res = [heapq.heappop(pq) for _ in range(len(pq))]
    return res

def max_heap(arr):
    """Return sorted list using max-heap (negation trick)"""
    pq = []
    for x in arr: heapq.heappush(pq, -x)
    res = [-heapq.heappop(pq) for _ in range(len(pq))]
    return res

# ---------- BINARY SEARCH ----------
def binary_search(arr, target):
    """Return index of target or -1"""
    left, right = 0, len(arr)-1
    while left <= right:
        mid = (left + right)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid+1
        else:
            right = mid-1
    return -1

# ---------- TREE / BINARY TREE ----------
class TreeNode:
    """Binary Tree Node"""
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# Tree Traversals
def preorder(node):
    if not node: return
    print(node.val, end=' ')
    preorder(node.left)
    preorder(node.right)

def inorder(node):
    if not node: return
    inorder(node.left)
    print(node.val, end=' ')
    inorder(node.right)

def postorder(node):
    if not node: return
    postorder(node.left)
    postorder(node.right)
    print(node.val, end=' ')

def bfs_tree(root):
    """Level order traversal of tree"""
    if not root: return
    q = deque([root])
    while q:
        node = q.popleft()
        print(node.val, end=' ')
        if node.left: q.append(node.left)
        if node.right: q.append(node.right)

# ---------- GRAPH ----------
class Graph:
    """Directed graph using adjacency list"""
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def dfs(self, start):
        visited = set()
        def dfs_util(node):
            if node in visited: return
            visited.add(node)
            print(node, end=' ')
            for nei in self.graph[node]:
                dfs_util(nei)
        dfs_util(start)

    def bfs(self, start):
        visited = set([start])
        q = deque([start])
        while q:
            node = q.popleft()
            print(node, end=' ')
            for nei in self.graph[node]:
                if nei not in visited:
                    visited.add(nei)
                    q.append(nei)

# ---------- DYNAMIC PROGRAMMING ----------
def memoize(f):
    """Memoization decorator for recursive DP"""
    cache = {}
    def wrapper(*args):
        if args in cache:
            return cache[args]
        res = f(*args)
        cache[args] = res
        return res
    return wrapper

def dp_tabulation(n, base_cases, transition):
    """
    Tabulation (bottom-up) DP template
    - n: size of problem
    - base_cases: dict {index: value} for starting values
    - transition: function f(dp, i) to calculate dp[i] from previous dp values
    """
    dp = [0]*(n+1)
    for idx, val in base_cases.items():
        dp[idx] = val
    for i in range(n+1):
        dp[i] = transition(dp, i)
    return dp

# ---------- OOP STARTER ----------
class Person:
    """Example base class"""
    def __init__(self, name:str, age:int):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, I am {self.name} and {self.age} years old.")

class Student(Person):
    """Example derived class"""
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade = grade

    def greet(self):
        print(f"Hi, I'm {self.name}, grade {self.grade}.")

# ---------- MAIN (EXAMPLES) ----------
if __name__ == "__main__":
    arr = [5,1,3]
    print("Min Heap:", min_heap(arr))
    print("Max Heap:", max_heap(arr))
    print("Prefix Sum:", prefix_sum(arr))
    print("Max sum subarray of size 2:", max_sum_subarray(arr, 2))

    # Tree example
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    print("\nPreorder Tree Traversal:")
    preorder(root)
    print("\nBFS Tree Traversal:")
    bfs_tree(root)

    # Graph example
    g = Graph()
    g.add_edge(0,1)
    g.add_edge(0,2)
    g.add_edge(1,2)
    g.add_edge(2,0)
    g.add_edge(2,3)
    print("\nDFS Graph Traversal:")
    g.dfs(0)
    print("\nBFS Graph Traversal:")
    g.bfs(0)

    # OOP example
    s = Student("Alice",20,"A")
    s.greet()
