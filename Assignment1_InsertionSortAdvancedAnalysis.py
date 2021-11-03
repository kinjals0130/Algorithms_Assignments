#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

#function purposes to count the inversions that happen during merge sort
def inversion_count(arr, arrlength):
    #create a temp array to store the sorted array from the merge function
    #number of indexes in the array depends on the length of the given array
    temp_arr = [0]*arrlength
    #pass 4 arguments
    return mergeSort(arr, temp_arr, 0, arrlength-1)
 

#function uses merge sort to get the number of inversions 
#mergeSort accepts 4 arguments which are passed form the inversion_count function 
def mergeSort(arr, temp_arr, left, right):
    
    #inversions is a counter that stores the number of inversions  
    inversions = 0
    #middle is calculated to split the 2 subarrays 
    middle = (left + right)//2
 
    #make a recursive call if the leftmost index is less than the rightmost array 
    if left < right:
 
        #calculate the number of inversions in the left subarray
        inversions += mergeSort(arr, temp_arr, left, middle)
        
        #calculate the inversions in the right subarray
        inversions += mergeSort(arr, temp_arr, middle + 1, right)
 
        #merge the two subarrays into a sorted array
        inversions += mergeArrays(arr, temp_arr, left, middle, right)
        
    return inversions

#function merges two subarrays into one single sorted array
def mergeArrays(arr, temp_arr, left, middle, right):
    
    #starting index's of the left and right subarray
    indexLeftArr = left         
    indexrightArr = middle + 1  
    #starting index of the array to be sorted 
    toBesortedArr = left
    #inversions counter            
    inversions = 0              
 

    #while loop used to make sure that the index of the left and right subarrays dont        #pass their limits
    while indexLeftArr <= middle and indexrightArr <= right:
 
        #checks if the array at index of the left subarray is less than the array at             #index of the right subarray 
        if arr[indexLeftArr] <= arr[indexrightArr]:
            #no inversions happen 
            temp_arr[toBesortedArr] = arr[indexLeftArr]
            toBesortedArr += 1
            indexLeftArr += 1
            
        #else if > or >= then inversions will happen
        else:
            temp_arr[toBesortedArr] = arr[indexrightArr]
            inversions += (middle-indexLeftArr + 1)
            toBesortedArr += 1
            indexrightArr += 1
 
    #copy the left subarray into the temporary array
    while indexLeftArr <= middle:
        temp_arr[toBesortedArr] = arr[indexLeftArr]
        toBesortedArr += 1
        indexLeftArr += 1
 
    #copy the right subarray into the temporary array
    while indexrightArr <= right:
        temp_arr[toBesortedArr] = arr[indexrightArr]
        toBesortedArr += 1
        indexrightArr += 1
 
    #tranfer the elements from the temporary array into the sorted array
    for i in range(left, right + 1):
        arr[i] = temp_arr[i]
         
    return inversions


    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))
        
        arrlength = len(arr)
        result = inversion_count(arr, arrlength)

              
        #result = insertionSort(arr)

        fptr.write(str(result) + '\n')

    fptr.close()
