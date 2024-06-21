 #Write a program in python to implement Merge Sort. (Note: Use of object oriented paradigm is compulsory)
 
 
 class MergeSort:
    def __init__(self, arr):
        self.arr = arr

    def merge_sort(self):
        if len(self.arr) > 1:
            mid = len(self.arr) // 2
            left_half = self.arr[:mid]
            right_half = self.arr[mid:]

            left_half_object = MergeSort(left_half)
            right_half_object = MergeSort(right_half)

            left_half_object.merge_sort()
            right_half_object.merge_sort()

            i = j = k = 0

            while i < len(left_half) and j < len(right_half):
                if left_half[i] < right_half[j]:
                    self.arr[k] = left_half[i]
                    i += 1
                else:
                    self.arr[k] = right_half[j]
                    j += 1
                k += 1

            while i < len(left_half):
                self.arr[k] = left_half[i]
                i += 1
                k += 1

            while j < len(right_half):
                self.arr[k] = right_half[j]
                j += 1
                k += 1

    def list_elements(self):
        return self.arr

# Create an instance of MergeSort
arr = [12, 11, 13, 5, 6, 7]
merge_sort = MergeSort(arr)

# Perform merge sort
merge_sort.merge_sort()

# List sorted elements
print(merge_sort.list_elements())
