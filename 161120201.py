import numpy as np
"""Good morning! Here's your coding interview problem for today.

This problem was asked by Stripe.

Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

You can modify the input array in-place."""
def main():
    print("main")
    list = [3, 4, -1, 1]
    list = [1, 2, 0]
    list = [1,2,3,4,4,7]
    list = sorted(list)
    print(checker(0, list))




def checker(number, array):

    if(array[number]) < 0: array.remove(array[number])
    print(array)
    if(array[number] == array[len(array) - 1]):
        print("Item ist last in list " + str(array[number]))
        return array[number] + 1
    if (array[number] - array[number + 1] == -1):
        return checker(number + 1, array)
    else:
        return array[number] + 1





if __name__ == "__main__":
    main()