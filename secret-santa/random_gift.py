from random import randint, choice
# This is a small program which aims to asign a secret santa ignoring couples. 

# list of people involved

receivers = {1:["Daniela","Stephen"],2:["Clémence","Rodrigo"],3:["Julie","Alejandro"],4:["Paulina"]} 
givers = {1:["Daniela","Stephen"],2:["Clémence","Rodrigo"],3:["Julie","Alejandro"],4:["Paulina"]} 

output_list = {}
random_family = 0
random_individual = ""

# This function deletes keys with empty values in dictionaries
def delete_empties(my_dict): 
    for key in list(my_dict): 
        if len(my_dict[key])==0 : 
            del my_dict[key] 

# This function chooses a random key and value within that key
def random_family_individual(dic1): 
    global random_family
    random_family = choice(list(dic1.keys()))
    global random_individual
    random_individual = randint(0, len(dic1[random_family])-1)
           
# Random choice logic
for family in list(givers):
    for individual in list(givers[family]): # we are treating every member individually through this nest
        random_family_individual(receivers)
        while random_family == family:
            random_family_individual(receivers)
        output_list[individual]=receivers[random_family][random_individual]
        del receivers[random_family][random_individual] 
        del givers[family][givers[family].index(individual)]
        delete_empties(receivers) 
        delete_empties(givers)
print(output_list)

f = open("gifts_2020.txt", "w")
f.write(repr(output_list))
f.close()
