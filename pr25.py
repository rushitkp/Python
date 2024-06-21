#Write a program in python to implement Fibonacci Series and Factorial using memo. (i.e. FastFibo &FastFact)
#(Note: Use of object oriented paradigm is compulsory.)


class Memo:
    def __init__(self):
        self.memo = {}

    def fast_fibo(self, n):
        if n in self.memo:
            return self.memo[n]

        if n <= 1:
            result = n
        else:
            result = self.fast_fibo(n-1) + self.fast_fibo(n-2)

        self.memo[n] = result
        return result

    def fast_fact(self, n):
        if n in self.memo:
            return self.memo[n]

        if n == 0:
            result = 1
        else:
            result = n * self.fast_fact(n-1)

        self.memo[n] = result
        return result

# Create an instance of Memo
memo = Memo()

# Calculate Fibonacci series using memoization
print([memo.fast_fibo(i) for i in range(10)])

# Calculate Factorial using memoization
print([memo.fast_fact(i) for i in range(10)])
