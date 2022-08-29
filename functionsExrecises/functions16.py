import random

def rand_Numbers(numbers:list, size = 10, low =1 , high = 100):
    """Gets an empty list , insert random numbers to the list"""
    for i in range(size):
        numbers.append(random.randint(low,high))