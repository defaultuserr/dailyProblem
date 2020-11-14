#Good morning! Here's your coding interview problem for today.

#This problem was recently asked by Google.

#Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

#For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

import os
import sys
import argparse
import random
import numpy as np

def main():
    print("Hello World!")
    vet = [10, 15, 3, 7]
    npGod = np.array(vet)
    k = 8

    print("it is ture") if findProblemsolver(npGod.tolist(), 17)  else print("it is wrong")





def findProblemsolver(array, number):
    for item in array:
        temp = number - item
        if temp <= 0:
            continue
        if temp > 0:
            if temp in array:
                return True
    return False





if __name__ == "__main__":
    main()