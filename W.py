# Script to manually create a custom spatial weight matrix for a panel data set

# Import required modules

import numpy as np
import pandas as pd

# Declare filepaths to read and write to

filepath = 'C:/Users/User/Documents/Data/data.csv'
output = 'C:/Users/User/Documents/Data/W.csv'

# Read the data into a dataframe

data = pd.read_csv(filepath)

# Create a list of unique entries for all nations using the Country dataseries

nations = data.Country.unique()

# Create the binary spatial weight matrix W

W = np.zeros([len(nations),len(nations)])

for nation in nations:
    idx = nations.index(nation)
    print(nation)
    accepted = False
    while accepted != True:
        try:
            adjacencies = int(input('How many adjacencies? '))
            accepted = True
        except:
            continue
    for i in range(adjacencies):
        complete = False
        while complete == False:
            try:
                neighbor = input('Input next neighbor: ')
                check = nations.index(neighbor)
                print(check)
                complete = True
            except:
                continue
        W[idx][check] = 1

# Ensure symmetry of W (in cases of inconsistencies in the munual entry process)

for i in range(len(W)):
    for j in range(len(W[i])):
        if W[i][j] > 0:
            W[j][i] = W[i][j]
            
W = pd.DataFrame(W)

# Creating a spatial weight matrix for the full panel data set

W2 = np.zeros((len(data.Country),len(data.Country)))
W = np.ceil(W)
W = W.values
for i in range(len(data.Country)):
    id1 = nations.index(data.Country[i])
    for j in range(len(data.Country)):
        if data.Year[i] == data.Year[j]:
            id2 = nations.index(data.Country[j])
            W2[i,j] = W[id1,id2]
    s = sum(W2[i,:])
    if s > 0:
        W2[i,:] = W2[i,:] / s
        
SW = pd.DataFrame(W2)
SW.to_csv(output, index = False, header = False)

