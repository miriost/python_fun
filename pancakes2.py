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

def flip_sequence(seq, indexes, k,n):
    
    if :
        return flag, n
    print('Current sequence: ' + convert_bin_to_sign(seq) + 'Indexes to flip:' + str(indexes) + 'k: '+str(k))
    for index in indexes:
        newseq = seq.copy()
        for char in range(index, index+k):
            newseq[char] = not(newseq[char])
        if not False in newseq:
            print('Possible! Flip index %d in string %s' %(index, convert_bin_to_sign(seq)))    
            return(True,n)
        else:
            newindexes = np.where(newseq == False)[0]
            # reduce the indexes to only valid indexes- this should decrease with time
            newindexes = [i if i+k <= len(newseq) else None for i in newindexes]
            newindexes = [x for x in newindexes if x is not None]
            if not newindexes: #no more indexes to check
                print('Impossible')
                return(False,n)
            else:
                flag,n = flip_sequence(newseq, newindexes,k,False, n+1)          
                 
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
        binseq = convert_sign_to_bin(seq)
        k = int(k)
        solution = 'IMPOSSIBLE'
        if '-' not in seq:
            solution = 0
        elif '+' not in seq:
            if len(seq)%k == 0:
                solution = int(len(seq)/k)
            else:
                indexes = np.where(binseq==False)[0]
                indexes = [i if i+k < len(binseq) else None for i in indexes]
                indexes = [x for x in indexes if x is not None]   
                if not indexes:
                    solution = 'IMPOSSIBLE'
                else:
                    answer,n = flip_sequence(binseq, indexes, k, False, 1)
                    if answer:
                        solution = n
                    else:
                        solution = 'IMPOSSIBLE'
        print("Case #%d: %s %s %s"%(case+1, seq, k, str(solution)))
    return(None)        
             
if __name__ == '__main__':
    flip_pancakes('A-small-practice.in')
#==============================================================================
# ===============================================================================
#      a = '+++-++-+'
#      b = convert_sign_to_bin(a)
#      answer = flip_sequence(b, [3], 3)
#          
# ===============================================================================
# 
#==============================================================================
