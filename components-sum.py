#------------------------
#This program finds the components of a number in terms of addition. 
#"sums" are the sums that you are looking for and the "components" are the potential pieces of one of those sums.
#------------------------

import random, itertools, timeit


#PROBLEM INFORMATION INPUT
# ----------------
components = [119.98, 114.26, 1295, 97.57, 119, 121.78, 2.48, 4.96]

sums = [358.50, 1516.53]
# ----------------

def use_all_combis():
    combis = []
    allsums = {}
    for num in range(2, len(components)):  #the 2 here is because we need at least two components for any given sum
        for item in itertools.combinations(components, num):
            combis.append(item)
    for item in combis: 
        allsums[item] = round(sum(item),2)
    for key, value in allsums.items():
        if value in sums:
            print key, value
            
use_all_combis()



    