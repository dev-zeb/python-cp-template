from python_cp_template import dp_tabulation, memoize

@memoize
def fib(n):
    if n <= 1: return n
    return fib(n-1) + fib(n-2)

print("Fib(10):", fib(10))
print("Fib(50):", fib(50))

def fib_transition(dp, i):
    if i <= 1: return i
    return dp[i-1] + dp[i-2]

dp = dp_tabulation(50, {}, fib_transition)
print(dp[50])
