#!/usr/bin/env python
#-*- coding: utf-8 -*-

def sum(arr):
    if len(arr) == 0:
        return 0
    return arr[0] + sum(arr[1:])

if __name__ == '__main__':
    arr = []
    for n in range(10):
        arr.append(n)
    result = sum(arr)
    print(result)
