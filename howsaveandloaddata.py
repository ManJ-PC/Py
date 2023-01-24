# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 12:03:58 2022

@author: mcurral
"""

import pickle
import os
os.system("clear")

# Create a list
names = ["Angus Young", "Malcolm Young", "Bon Scott"]

# Print the list
print('Original List')
print(names)

# Save the list
pickle.dump(names, open("name.dat", "wb"))

# Change 
names.remove("Bon Scott")

# Print the list
print("Changed List")
print(names)

# Load the saved data
names = pickle.load(open("names.dat", "rb"))
#def register():

# Print the list
print("Original List")
print(names)
