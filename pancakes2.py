# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 21:22:05 2018

@author: mirio
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 12 12:28:28 2018

@author: miri-o
"""

import numpy as np


def convert_sign_to_bin(seq):
    conversion_dict = {'+':True, '-':False}
    outseq = np.array([])
    for char in seq:
        outseq = np.insert(outseq, len(outseq), conversion_dict[char])
    return outseq
    
    
def convert_bin_to_sign(seq):
    conversion_dict = {'True':'+', 'False': '-', 1:'+',0:'-'}
    outseq = ''
    for sign in seq:
        outseq = outseq+conversion_dict[sign]
    return outseq

def choose_best(solutions):
    # recieve a list of solutions and decide which one is the optimal one
    solutions_n = [x for x in solutions if x!=False]
    if solutions_n:
        return(min(solutions_n))
    else:
        return(False)
    
def flip_sequence(seq, index, k,n):
    
    #print('Current sequence: ' + convert_bin_to_sign(seq) + ' Index to flip:' + str(index) + ' k: '+str(k))

    newseq = seq.copy()
    for char in range(index, index+k):
        newseq[char] = not(newseq[char])
    if not False in newseq:
        #print('Possible! Flip index %d in string %s' %(index, convert_bin_to_sign(seq)))    
        return(n)
    else:
        newindexes = np.where(newseq == False)[0]
        # reduce the indexes to only valid indexes- this should decrease with time
        newindexes = [i if i+k <= len(newseq) else None for i in newindexes]
        newindexes = [x for x in newindexes if x is not None]
        if not newindexes: #no more indexes to check
        #    print('Impossible')
            return(False)
        else:
            solutions = [flip_sequence(newseq, i,k, n+1) for i in newindexes]
            best_solution = choose_best(solutions)
        #    print('intermidate result for %d: %s ' %(n+1, str(best_solution)))
            return best_solution 
def flip_pancakes(file):
    """
    Input:
        file
        

The first line of the input gives the number of test cases, T. T test cases follow. 
Each consists of one line with a string S and an integer K. 
S represents the row of pancakes: 
    each of its characters is either + (which represents a pancake that is initially happy side up) or 
    - (which represents a pancake that is initially blank side up).
Output

For each test case, output one line containing Case #x: y, where x is the test case number (starting from 1) 
and y is either IMPOSSIBLE if there is no way to get all the pancakes happy side up, 
or an integer representing the the minimum number of times you will need to use the oversized pancake flipper to do it. 
"""
    f = open(file).readlines()
    filelen = int(f[0])
    for case in (range(filelen)):
        seq = f[case+1]
        seq, k = seq.split(" ")
        k = int(k)
        binseq = convert_sign_to_bin(seq)
        newindexes = np.where(binseq == False)[0]
        # reduce the indexes to only valid indexes- this should decrease with time
        newindexes = [i if i+k <= len(binseq) else None for i in newindexes]
        newindexes = [x for x in newindexes if x is not None]
        answer = [flip_sequence(binseq, i, 3, 1) for i in newindexes]
        best_solution = choose_best(answer)
        print('best solution '+str(best_solution))  
#==============================================================================
#         k = int(k)
#         best_solution = False
#         if '-' not in seq:
#             best_solution = 0
#         elif '+' not in seq:
#             if len(seq)%k == 0:
#                 best_solution = int(len(seq)/k)
#         else:
#             indexes = np.where(binseq==False)[0]
#             indexes = [i if i+k <= len(binseq) else None for i in indexes]
#             indexes = [x for x in indexes if x is not None]   
#             if not indexes:
#                 best_solution = False
#             else:
#                 solutions = [flip_sequence(binseq, indx, k, n=1) for indx in indexes]
#                 best_solution = choose_best(solutions)
#         print("Case #%d: %s %s %s"%(case+1, seq, k, str(best_solution)))
#==============================================================================
    return(None)        
             
if __name__ == '__main__':
    flip_pancakes('A-small-practice.in')
   #flip_pancakes('1_example.txt')
#==============================================================================
# 
# 
#     a = '---+'
#     b = convert_sign_to_bin(a)
#     answer = [flip_sequence(b, i, 3, 1) for i in [0,1]]
#     best_solution = choose_best(answer)
#     print('best solution '+str(best_solution))     
# 
# 
# 
#==============================================================================
