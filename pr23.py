#Write a program in python to implement Bubble Sort. (Note: Use of object oriented paradigm is compulsory)


class BubbleSort:
    def __init__(self, arr):
        self.arr = arr

    def bubble_sort(self):
        n = len(self.arr)
        for i in range(n-1):
            for j in range(0, n-i-1):
                if self.arr[j] > self.arr[j+1]:
                    self.arr[j], self.arr[j+1] = self.arr[j+1], self.arr[j]

    def list_elements(self):
        return self.arr

# Create an instance of BubbleSort
arr = [64, 34, 25, 12, 22, 11, 90]
bubble_sort = BubbleSort(arr)

# Perform bubble sort
bubble_sort.bubble_sort()

# List sorted elements
print(bubble_sort.list_elements())
