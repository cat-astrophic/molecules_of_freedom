# This script performs the statistical analysis for Molecules of Freedom

# For clarity, 'Molecules of Freedom' is an idiotic catchphrase used by the 45th administration to reference natural gas

# Importing required modules

import pandas as pd
import statsmodels.api as stats
import pysal

# Loading the data ses and storing it in a dataframe

spatial_filepath = 'C:/Users/User/Documents/Data/MOF.csv'
sw_filepath = 'C:/Users/User/Documents/Data/MOF_W.csv'

spdata = pd.read_csv(spatial_filepath)
SW = pd.read_csv(sw_filepath, header = None)

# Creating dataframes for all regression models

# Endogenous variables

Y = spdata['Intensity']

# Exogenous variables

# Exogenous variables for spatial models -- will be called by pysal later on

Xsp1 = spdata[['Intensity_Lag', 'GDP', 'Renewable Energy', 'Coal Rents', 'Oil Rents', 'Crude Price', 'R&D', 'Tariff Rate']]
Xsp2 = spdata[['Intensity_Lag', 'GDP', 'Renewable Energy', 'Coal Rents', 'Oil Rents', 'Crude Price', 'R&D', 'Target Tariff']]

# Dataframes ready for baselines OLS regression

X1 = stats.add_constant(Xsp1)
X2 = stats.add_constant(Xsp2)

# Running OLS regression models

model1 = stats.OLS(Y, X1)
results1 = model1.fit()
print(results1.summary())
file = open('C:/Users/User/Documents/Data/MoF/model1.txt', 'w')
file.write(results1.summary().as_text())
file.close()

model2 = stats.OLS(Y, X2)
results2 = model2.fit()
print(results2.summary())
file = open('C:/Users/User/Documents/Data/MoF/model2.txt', 'w')
file.write(results2.summary().as_text())
file.close()

# Creating spatial weights matrix for spatial models

neighbs = []
for i in range(len(SW)):
    row = []
    for j in range(len(SW)):
        if SW[i][j] > 0:
            row.append(j)
    neighbs.append(row)
w_keys = [i for i in range(len(SW))]
w_d = dict(zip(w_keys, neighbs))
w = pysal.lib.weights.W(w_d)
w.transform = 'r'

# Running spatial lag model in pysal

sp1 = pysal.model.spreg.ML_Lag(Y.values[:,None], Xsp1.values, w = w, name_x = Xsp1.columns.tolist(), name_y = 'CO2 Intensity')
print(sp1.summary)
file = open('C:/Users/User/Documents/Data/MoF/splag1.txt', 'w')
file.write(sp1.summary)
file.close()

sp2 = pysal.model.spreg.ML_Lag(Y.values[:,None], Xsp2.values, w = w, name_x = Xsp2.columns.tolist(), name_y = 'CO2 Intensity')
print(sp2.summary)
file = open('C:/Users/User/Documents/Data/MoF/splag2.txt', 'w')
file.write(sp2.summary)
file.close()















