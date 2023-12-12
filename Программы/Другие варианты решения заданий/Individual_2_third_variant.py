#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys


if __name__ == '__main__':
    print("Good day! Please, enter 10 numbers.\n")
    elements = list(
        map(float, input("Remember to put some space between them:").split()))
    start = int(input("Please, enter the beginning of the range - "))
    end = int(input("Please, enter the ending of the range - "))
    in_range = sum(1 for i in elements if start <= i <= end)
    print("\nAmount of elements, that lie in your range is", in_range)
    elements_sum = sum(elements[elements.index(max(elements))+1:])
    print("\nSum of elements after maximal element = ", elements_sum)
    elements.sort(key=lambda x: abs(x), reverse=True)
    print("\nTransformed list: ", elements)
