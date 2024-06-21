#Write a program in python to implement simple interest and compound interest values on chart using PyLab.Show the difference between both. (Note: Use of object oriented paradigm is compulsory.)

import pr14 as plt

class InterestCalculator:
    def __init__(self, principal, rate, time):
        self.principal = principal
        self.rate = rate
        self.time = time

    def simple_interest(self):
        return (self.principal * self.rate * self.time) / 100

    def compound_interest(self):
        return self.principal * ((1 + self.rate / 100) ** self.time - 1)

    def plot_interest(self):
        time_range = range(1, self.time + 1)
        simple_interest_values = [self.simple_interest() for _ in time_range]
        compound_interest_values = [self.compound_interest() for _ in time_range]

        plt.plot(time_range, simple_interest_values, label='Simple Interest')
        plt.plot(time_range, compound_interest_values, label='Compound Interest')
        plt.xlabel('Time (years)')
        plt.ylabel('Interest (rupees)')
        plt.title('Simple vs Compound Interest')
        plt.legend()
        plt.show()

# Input values
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the annual interest rate: "))
time = int(input("Enter the time period (in years): "))

# Create an instance of InterestCalculator
calculator = InterestCalculator(principal, rate, time)

# Calculate and display simple interest and compound interest
simple_interest = calculator.simple_interest()
compound_interest = calculator.compound_interest()
print(f"Simple Interest: Rs. {simple_interest:.2f}")
print(f"Compound Interest: Rs. {compound_interest:.2f}")

# Plot the interest values
calculator.plot_interest()
