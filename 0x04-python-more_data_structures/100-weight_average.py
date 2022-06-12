#!/usr/bin/python3

def weight_average(my_list=[]):
    """
    Finds the weighted average of all integers tuple (<score>, <weight>)

    Args:
        my_list: list of integer tuples

    Return: weighted average
    """
    average = sum([a * b for (a, b) in my_list])
    total = sum([b for (a, b) in my_list])

    return average / total if len(my_list) else 0
