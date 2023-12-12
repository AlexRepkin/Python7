#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys


if __name__ == '__main__':
    print("Good day! Please, enter 10 numbers.\n")
    elements = list(
        map(float, input("Remember to put some space between them:").split()))
    start = int(input("Please, enter the beginning of the range - "))
    end = int(input("Please, enter the ending of the range - "))
    in_range = 0
    max_element = max(elements)
    found = False
    elements_sum = 0
    for i in elements:
        if start <= i <= end:
            in_range += 1
        if found == True:
            print(i, end=" ")
            elements_sum += i
        elif max_element == i:
            print("We've found maximal element in list - ",
                  max_element, " values after it: ", end="")
            found = True
    print("\nTheir sum = ", elements_sum)
    print("\n\nAmount of elements, that lie in your range is", in_range)
    elements.sort(key=lambda x: abs(x), reverse=True)
    print("\nTransformed list: ", elements)
