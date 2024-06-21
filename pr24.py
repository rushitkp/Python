#Write a program in python to implement 0/1 Knapsack algorithm. (Note: Use of object oriented paradigm iscompulsory.)


class Knapsack:
    def __init__(self, weights, values, capacity):
        self.weights = weights
        self.values = values
        self.capacity = capacity
        self.n = len(weights)
        self.dp = [[-1 for _ in range(capacity + 1)] for _ in range(self.n + 1)]

    def knapsack(self, i, w):
        if i == 0 or w == 0:
            return 0

        if self.dp[i][w] != -1:
            return self.dp[i][w]

        if self.weights[i - 1] <= w:
            self.dp[i][w] = max(self.values[i - 1] + self.knapsack(i - 1, w - self.weights[i - 1]), self.knapsack(i - 1, w))
        else:
            self.dp[i][w] = self.knapsack(i - 1, w)

        return self.dp[i][w]

# Create an instance of Knapsack
weights = [10, 20, 30]
values = [60, 100, 120]
capacity = 50
knapsack = Knapsack(weights, values, capacity)

# Perform 0/1 knapsack
max_value = knapsack.knapsack(knapsack.n, knapsack.capacity)

# Print the maximum value
print(max_value)
