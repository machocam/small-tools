# Goal
This is a small secret santa project with some specificities for my family.
The specifics follow: 
1. No family should gift within themselves (there would be no surprise)
2. Everyone should get and give a gift
3. Not implemented as of 2020-11-28 - no family should give gifts to another family: 
All members of family 1 give gifts to all members of family 2. 


# Use 
1. Put the name of all individuals in every given family in a [dictionary](https://docs.python.org/3/tutorial/datastructures.html).
The format should be the following: {family_number : member1, member2} 
2. Copy the same values in the receviers and givers variables
2. Run the program with "python3 random_gift.py"
3. It will output in a file in the same directory the results

# Interpretation of results 
The results are also dictionaries. Where the "key" is the giver and the "value" the receiver. 
