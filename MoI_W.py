# Script to manually create a custom spatial weight matrix for a panel data set

# Import required modules

import numpy as np
import pandas as pd

# Declare filepaths to read and write to

filepath = 'C:/Users/User/Documents/Data/MoI.csv' # Panel data set
output = 'C:/Users/User/Documents/Data/MoI_W.csv' # Final spatial weights matrix

# Read the data into a dataframe

data = pd.read_csv(filepath)

# Create a list of unique entries for all nations using the Country dataseries

nations = data.Country.unique()

# Create the binary spatial weight matrix W

W = np.zeros([len(nations),len(nations)])

for nation in nations:
    
    idx = np.where(nations == nation)[0][0]
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
                check = np.where(nations == neighbor)[0][0]
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
            
# Create dataframe

W = pd.DataFrame(W)

# Creating a spatial weight matrix for the full panel data set

W2 = np.zeros((len(data.Country),len(data.Country)))
W = W.values

for i in range(len(data.Country)):
    
    id1 = np.where(nations == data.Country[i])[0][0]
    
    for j in range(len(data.Country)):
        
        if data.Year[i] == data.Year[j]:
            
            id2 = np.where(nations == data.Country[j])[0][0]
            W2[i,j] = W[id1,id2]

# Normalize the spatial weights matrix and write it to file

for i in range(len(W)):
    
    s = sum(W[i,:])
    W[i,:] = W[i,:] / s

W = pd.DataFrame(W)
W.to_csv(output, index = False, header = False)

