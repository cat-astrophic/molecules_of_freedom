# This script performs the statistical analysis for Molecules of Freedom

# For clarity, 'Molecules of Freedom' is an idiotic catchphrase used by the 45th administration to reference natural gas

# Importing required modules

import pandas as pd
import statsmodels.api as stats
import pysal

# Loading the data ses and storing it in a dataframe

spatial_filepath = 'C:/Users/User/Documents/Data/MoF/MOF.csv'
sw_filepath = 'C:/Users/User/Documents/Data/MoF/MOF_W.csv'

spdata = pd.read_csv(spatial_filepath)
SW = pd.read_csv(sw_filepath, header = None)

# Creating dataframes for all regression models

# Endogenous variables

Y = spdata['Intensity']

# Exogenous variables

# Exogenous variables for spatial models -- will be called by pysal later on

Xsp1 = spdata[['Intensity_Lag', 'GDP', 'Renewable Energy', 'R&D', 'Tariff Rate']]
Xsp2 = spdata[['Intensity_Lag', 'GDP', 'Renewable Energy', 'R&D', 'Target Tariff']]
Xsp3 = spdata[['GDP', 'Renewable Energy', 'R&D', 'Tariff Rate']]
Xsp4 = spdata[['GDP', 'Renewable Energy', 'R&D', 'Target Tariff']]

# Dataframes ready for baselines OLS regression

X1 = stats.add_constant(Xsp1)
X2 = stats.add_constant(Xsp2)
X3 = stats.add_constant(Xsp3)
X4 = stats.add_constant(Xsp4)

# Running OLS regression models

model1 = stats.OLS(Y, X1)
results1 = model1.fit()
print(results1.summary())
file = open('C:/Users/User/Documents/Data/MoF/MoF/model1.txt', 'w')
file.write(results1.summary().as_text())
file.close()

model2 = stats.OLS(Y, X2)
results2 = model2.fit()
print(results2.summary())
file = open('C:/Users/User/Documents/Data/MoF/MoF/model2.txt', 'w')
file.write(results2.summary().as_text())
file.close()

model3 = stats.OLS(Y, X3)
results3 = model3.fit()
print(results3.summary())
file = open('C:/Users/User/Documents/Data/MoF/MoF/model3.txt', 'w')
file.write(results3.summary().as_text())
file.close()

model4 = stats.OLS(Y, X4)
results4 = model4.fit()
print(results4.summary())
file = open('C:/Users/User/Documents/Data/MoF/MoF/model4.txt', 'w')
file.write(results4.summary().as_text())
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

# Running spatial model in pysal

sp1 = pysal.model.spreg.ML_Lag(Y.values[:,None], Xsp1.values, w = w, name_x = Xsp1.columns.tolist(), name_y = 'CO2 Intensity')
print(sp1.summary)
file = open('C:/Users/User/Documents/Data/MoF/MoF/sp1.txt', 'w')
file.write(sp1.summary)
file.close()

sp2 = pysal.model.spreg.ML_Lag(Y.values[:,None], Xsp2.values, w = w, name_x = Xsp2.columns.tolist(), name_y = 'CO2 Intensity')
print(sp2.summary)
file = open('C:/Users/User/Documents/Data/MoF/MoF/sp2.txt', 'w')
file.write(sp2.summary)
file.close()

sp3 = pysal.model.spreg.ML_Lag(Y.values[:,None], Xsp3.values, w = w, name_x = Xsp3.columns.tolist(), name_y = 'CO2 Intensity')
print(sp3.summary)
file = open('C:/Users/User/Documents/Data/MoF/MoF/sp3.txt', 'w')
file.write(sp3.summary)
file.close()

sp4 = pysal.model.spreg.ML_Lag(Y.values[:,None], Xsp4.values, w = w, name_x = Xsp4.columns.tolist(), name_y = 'CO2 Intensity')
file = open('C:/Users/User/Documents/Data/MoF/MoF/sp4.txt', 'w')
print(sp4.summary)
file.write(sp4.summary)
file.close()

