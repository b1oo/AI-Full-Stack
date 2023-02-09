""" A bogo sort is an inefficient sorting algorithm, also known as a "stupid sort". Here's an example implementation in Python """
import random

def bogoSort(arr):
    while not isSorted(arr):
        random.shuffle(arr)

def isSorted(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True

arr = [3, 2, 4, 1, 5]
bogoSort(arr)
print("Sorted array:", arr)
