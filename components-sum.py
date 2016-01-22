#------------------------
#This program finds the components of a number in terms of addition. 
#"sums" are the sums that you are looking for and the "components" are the potential pieces of one of those sums.
#------------------------

import random

#PROBLEM INFORMATION INPUT
# ----------------
components = [119.98,
           114.26,
           1295,
           97.57,
           119,
           121.78,
           2.48,
           4.96
          ]

sums = [358.50, 1516.53]
# ----------------

mysum = 0
while mysum not in sums:
    myrange = range(len(components))
    mysum = 0
    while len(myrange)>0 and mysum not in sums: 
        randint = random.choice(myrange)
        mysum += components[randint]
        myrange.remove(randint)

mysum_range = [components[x] for x in range(len(components)) if x not in myrange] #outputs the components of the sum found in sums

print mysum, mysum_range


            

    