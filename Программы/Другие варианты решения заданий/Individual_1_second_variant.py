#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys


if __name__ == '__main__':
    print("Good day! Please, enter 10 numbers.\n")
    a = list(map(int, input("Remember to put some space between them:").split()))
    if len(a) != 10:
        print("Wrong list size!", file=sys.stderr)
        exit(1)
    minimal = a.index(min(a))
    if a.count(a[minimal]) > 1:
        print("List contains several identical minimum values!", file=sys.stderr)
        exit(1)
    a[minimal], a[-1] = a[-1], a[minimal]
    print(a)
