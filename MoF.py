# This script performs the statistical analysis for Molecules of Freedom

# For clarity, 'Molecules of Freedom' is an idiotic catchphrase used by the 45th administration to reference natural gas

# Importing required modules

import numpy as np
import pandas as pd
import statsmodels.api as stats
import pysal

# Loading the data ses and storing it in a dataframe

filepath = 'C:/Users/User/Documents/Data/MOF-R&D.csv'
spatial_filepath = 'C:/Users/User/Documents/Data/MOF-R&D_no_islands.csv'
sw_filepath = 'C:/Users/User/Documents/Data/MOF_W.csv'

data = pd.read_csv(filepath)
spdata = pd.read_csv(spatial_filepath)
SW = pd.read_csv(sw_filepath, header = None)

# Creating dataframes for all regression models

# Endogenous variables

Y = data['CO2-Intensity']
Ysp = spdata['CO2-Intensity']

# Exogenous variables

# Exogenous variables for baseline models

X1 = data[['GDP', 'GDP2', 'Renewable Energy', 'R&D', 'Tariff Rate']]
X2 = data[['GDP', 'Renewable Energy', 'R&D', 'Tariff Rate']]
X3 = data[['CO2-Intense-lag', 'GDP', 'GDP2', 'Renewable Energy', 'R&D', 'Tariff Rate']]
X4 = data[['CO2-Intense-lag', 'GDP', 'Renewable Energy', 'R&D', 'Tariff Rate']]

# Exogenous variables for spatial models -- will be called by pysal alter on

Xsp1 = spdata[['GDP', 'GDP2', 'Renewable Energy', 'R&D', 'Tariff Rate']]
Xsp2 = spdata[['GDP', 'Renewable Energy', 'R&D', 'Tariff Rate']]
Xsp3 = spdata[['CO2-Intense-lag', 'GDP', 'GDP2', 'Renewable Energy', 'R&D', 'Tariff Rate']]
Xsp4 = spdata[['CO2-Intense-lag', 'GDP', 'Renewable Energy', 'R&D', 'Tariff Rate']]

# Exogenous spatial lags

W1 = np.dot(SW, Xsp1)
W2 = np.dot(SW, Xsp2)
W3 = np.dot(SW, Xsp3)
W4 = np.dot(SW, Xsp4)

W1 = pd.DataFrame(W1, columns = Xsp1.columns)
W2 = pd.DataFrame(W2, columns = Xsp2.columns)
W3 = pd.DataFrame(W3, columns = Xsp3.columns)
W4 = pd.DataFrame(W4, columns = Xsp4.columns)

# Exogenous spatial lag models -- will be called by pysal later on

WXsp1 = pd.concat([Xsp1, W1], axis = 1)
WXsp2 = pd.concat([Xsp2, W2], axis = 1)
WXsp3 = pd.concat([Xsp3, W3], axis = 1)
WXsp4 = pd.concat([Xsp4, W4], axis = 1)

# Dataframes ready for baselines OLS regression

X1 = stats.add_constant(X1)
X2 = stats.add_constant(X2)
X3 = stats.add_constant(X3)
X4 = stats.add_constant(X4)

# Dataframes ready for spatial models

WX1 = stats.add_constant(WXsp1)
WX2 = stats.add_constant(WXsp2)
WX3 = stats.add_constant(WXsp3)
WX4 = stats.add_constant(WXsp4)

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


model3 = stats.OLS(Y, X3)
results3 = model3.fit()
print(results3.summary())
file = open('C:/Users/User/Documents/Data/MoF/model3.txt', 'w')
file.write(results3.summary().as_text())
file.close()

model4 = stats.OLS(Y, X4)
results4 = model4.fit()
print(results4.summary())
file = open('C:/Users/User/Documents/Data/MoF/model4.txt', 'w')
file.write(results4.summary().as_text())
file.close()

# Running exogenous spatial lag regression models

exomodel1 = stats.OLS(Ysp, WX1)
results1 = exomodel1.fit()
print(results1.summary())
file = open('C:/Users/User/Documents/Data/MoF/exomodel1.txt', 'w')
file.write(results1.summary().as_text())
file.close()

exomodel2 = stats.OLS(Ysp, WX2)
results2 = exomodel2.fit()
print(results2.summary())
file = open('C:/Users/User/Documents/Data/MoF/exomodel2.txt', 'w')
file.write(results2.summary().as_text())
file.close()

exomodel3 = stats.OLS(Ysp, WX3)
results3 = exomodel3.fit()
print(results3.summary())
file = open('C:/Users/User/Documents/Data/MoF/exomodel3.txt', 'w')
file.write(results3.summary().as_text())
file.close()

exomodel4 = stats.OLS(Ysp, WX4)
results4 = exomodel4.fit()
print(results4.summary())
file = open('C:/Users/User/Documents/Data/MoF/exomodel4.txt', 'w')
file.write(results4.summary().as_text())
file.close()

# Running spatial error models with exogenous spatial lag

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

sperror1 = pysal.model.spreg.ML_Error(Ysp.values[:,None], WXsp1.values, w = w, name_x = WXsp1.columns.tolist(), name_y = 'CO2 Intensity')
print(sperror1.summary)
file = open('C:/Users/User/Documents/Data/MoF/sperror1.txt', 'w')
file.write(sperror1.summary)
file.close()

sperror2 = pysal.model.spreg.ML_Error(Ysp.values[:,None], WXsp2.values, w = w, name_x = WXsp2.columns.tolist(), name_y = 'CO2 Intensity')
print(sperror2.summary)
file = open('C:/Users/User/Documents/Data/MoF/sperror2.txt', 'w')
file.write(sperror2.summary)
file.close()

sperror3 = pysal.model.spreg.ML_Error(Ysp.values[:,None], WXsp3.values, w = w, name_x = WXsp3.columns.tolist(), name_y = 'CO2 Intensity')
print(sperror3.summary)
file = open('C:/Users/User/Documents/Data/MoF/sperror3.txt', 'w')
file.write(sperror3.summary)
file.close()

sperror4 = pysal.model.spreg.ML_Error(Ysp.values[:,None], WXsp4.values, w = w, name_x = WXsp4.columns.tolist(), name_y = 'CO2 Intensity')
print(sperror4.summary)
file = open('C:/Users/User/Documents/Data/MoF/sperror4.txt', 'w')
file.write(sperror4.summary)
file.close()

# Running full spatial model in pysal

sp1 = pysal.model.spreg.ML_Lag(Ysp.values[:,None], WXsp1.values, w = w, name_x = WXsp1.columns.tolist(), name_y = 'CO2 Intensity')
print(sp1.summary)
file = open('C:/Users/User/Documents/Data/MoF/sp1.txt', 'w')
file.write(sp1.summary)
file.close()

sp2 = pysal.model.spreg.ML_Lag(Ysp.values[:,None], WXsp2.values, w = w, name_x = WXsp2.columns.tolist(), name_y = 'CO2 Intensity')
print(sp2.summary)
file = open('C:/Users/User/Documents/Data/MoF/sp2.txt', 'w')
file.write(sp2.summary)
file.close()

sp3 = pysal.model.spreg.ML_Lag(Ysp.values[:,None], WXsp3.values, w = w, name_x = WXsp3.columns.tolist(), name_y = 'CO2 Intensity')
print(sp3.summary)
file = open('C:/Users/User/Documents/Data/MoF/sp3.txt', 'w')
file.write(sp3.summary)
file.close()

sp4 = pysal.model.spreg.ML_Lag(Ysp.values[:,None], WXsp4.values, w = w, name_x = WXsp4.columns.tolist(), name_y = 'CO2 Intensity')
print(sp4.summary)
file = open('C:/Users/User/Documents/Data/MoF/sp4.txt', 'w')
file.write(sp4.summary)
file.close()

