#===----- Hashsets -----===# 
#Initializing Hashset
mySet = set()

#Adding to a hashset
mySet.add(1)
mySet.add(2)
mySet.add(3)

#Removing from hashset
mySet.remove(3)


#Checking if something is in a hashset
print(1 in mySet) #Prints True
print(3 in mySet) #Prints False

#Great for conditionals
if (1 in mySet):
    mySet.remove(2)

#Converting a list to a set
convertedSet = set([2,3,4,5])

#Set comprehension
comprehensionSet = {i for i in range(5,10)}

#===----- Hashmaps -----===# 
# Stored in pairs: {key : value}
#Initializing HashMap
myMap = {}

#Adding to hashmap
#Note: single/double quotation marks can 
#be used interchangable to denote strings

myMap["George Washington"] = 1789
myMap = {'MX5 Miata' : 2015, "Ford Bronco" : 2022}

#Removing from hashmap
myMap.pop("Ford Bronco")

#Format of the hashmap: {'Example' : 0}
print(myMap)

#Length is calculated by pairs
mapLength = len(myMap) #Prints 1

#Using key to update value
myMap['MX5 Miata'] = 2019

#Using key to grab values
value = myMap['MX5 Miata'] #stores 2019

#Using get() to grab values
#   .get(key, default)
#   If the key is not found, it returns the default value
value = myMap.get('Ford Bronco', 789)  #Couldn't find bronco, returns 789
value = myMap.get('MX5 Miata', 0) #returns 2019

# Dict comprehension
myMap = { i: 2*i for i in range(3) }
print(myMap) # {0: 0, 1: 2, 2: 4}

# Looping through all the keys in a hashmap
myMap = {"checkingBalance" : 6000, "savingsBalance" : 100}
for key in myMap:
    print(key, myMap[key]) # checkingBalance 600, savingsBalance 100

#Looping through all the values of a hashmap
for val in myMap.values(): # 6000, 100
    print(val)

for key, val in myMap.items(): #checkingBalance 6000, savingsBalance 100
    print(key, val)

