#!/usr/bin/env python
#-*- coding: utf-8 -*-

def findMin(arr):
    if (len(arr)== 0):
        return None
    min_index = 0;
    for i in range(1, len(arr)):
        if(arr[i]< arr[min_index]):
            min_index = i
    return min_index

def order(arr):
    new_arr = []
    for n in range(len(arr)):
        min = findMin(arr)
        if(min != None):
            new_arr.append(arr.pop(min))

    return new_arr

if __name__=='__main__':
    arr = []
    for n in range(100):
        arr.append(100 - n)
    result = order(arr)
    print(result)
