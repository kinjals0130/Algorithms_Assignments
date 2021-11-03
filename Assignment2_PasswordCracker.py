#!/bin/python3

import math
import os
import random
import re
import sys

sys.setrecursionlimit(10000)

#
# Complete the 'passwordCracker' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING_ARRAY passwords
#  2. STRING loginAttempt
#

#holds the passwords in a dictionary
password_dict = {}

def process(passwords, loginAttempt):
    global password_dict
    
    #if the length of the loginAttempt is 0 we return True to 
    #say it is the end of the array and return an empty array 
    if len(loginAttempt) == 0:
        return True, []
    
    #if the solution is in the dictionary return False and return empty array
    if loginAttempt in password_dict:
        return False, []
    
    #loop through all the passwords
    for password in passwords:
        
        #if the login attempt starts with the password, we need to call the function              again recursively, shifting the length of the password to the end
        if loginAttempt.startswith(password):
            solution, result = process(passwords, loginAttempt[len(password):])
            
            #if the solution is valid then return True and the password concatenated                  with the result 
            if solution: 
                #add the solution to the dictionary
                password_dict[loginAttempt] = True
                return True, [password] + result
            
    #return False and empty array if there are no matches found at all      
    return False, []
    
def passwordCracker(passwords, loginAttempt):
    
    #initialize the password dictionary
    global password_dict
    password_dict = {}
    
    #call the process function and pass the passwords and login attempt lists
    solution, result = process(passwords, loginAttempt)
    
    #if we have a solution, return the result 
    if solution:
        return " ".join(result)
    
    #if no solution is found, return wrong password
    return "WRONG PASSWORD"
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())
        passwords = input().rstrip().split()
        loginAttempt = input()
        result = passwordCracker(passwords, loginAttempt)
        fptr.write(result + '\n')

    fptr.close()
