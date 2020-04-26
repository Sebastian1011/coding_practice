#!/usr/bin/env python
#-*- coding: utf-8 -*-

def search(low, high, arr, target):
    print(low, high)
    mid = (low + high)//2
    if (arr[mid]==target):
        return mid
    if low == high:
        return None
    if(arr[mid] > target):
        return search(low, mid-1, arr, target)
    if(arr[mid]< target):
        return search(mid+1, high, arr, target)
if __name__ == '__main__':
    arr = []
    for n in range(100000):
        arr.append(n)
    result = search(0, len(arr)-1, arr, 50)
    print(result)
