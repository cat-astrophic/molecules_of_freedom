# This script performs the statistical analysis for Molecules of Freedom

# For clarity, 'Molecules of Freedom' is an idiotic catchphrase used by the 45th administration to reference natural gas

# Importing required modules

import numpy as np
import pandas as pd
import statsmodels.api as stats
import pysal

# Loading the data ses and storing it in a dataframe

spatial_filepath = 'C:/Users/User/Documents/Data/MOF-R&D_no_islands.csv'
sw_filepath = 'C:/Users/User/Documents/Data/MOF_W.csv'

spdata = pd.read_csv(spatial_filepath)
SW = pd.read_csv(sw_filepath, header = None)

# Creating dataframes for all regression models

# Endogenous variables

Ysp = spdata['CO2-Intensity']

# Exogenous variables

# Exogenous variables for spatial models -- will be called by pysal later on

Xsp1 = spdata[['GDP', 'GDP2', 'Renewable Energy', 'R&D', 'Tariff Rate']]
Xsp2 = spdata[['GDP', 'Renewable Energy', 'R&D', 'Tariff Rate']]
Xsp3 = spdata[['GDP', 'GDP2', 'Renewable Energy', 'R&D', 'Target Tariff']]
Xsp4 = spdata[['GDP', 'Renewable Energy', 'R&D', 'Target Tariff']]
Xsp5 = spdata[['GDP', 'GDP2', 'Renewable Energy', 'R&D', 'Tariff Rate', 'Target Tariff']]
Xsp6 = spdata[['GDP', 'Renewable Energy', 'R&D', 'Tariff Rate', 'Target Tariff']]

# Exogenous spatial lags

W1 = np.dot(SW, Xsp1)
W2 = np.dot(SW, Xsp2)
W3 = np.dot(SW, Xsp3)
W4 = np.dot(SW, Xsp4)
W5 = np.dot(SW, Xsp5)
W6 = np.dot(SW, Xsp6)

W1 = pd.DataFrame(W1, columns = Xsp1.columns)
W2 = pd.DataFrame(W2, columns = Xsp2.columns)
W3 = pd.DataFrame(W3, columns = Xsp3.columns)
W4 = pd.DataFrame(W4, columns = Xsp4.columns)
W5 = pd.DataFrame(W5, columns = Xsp5.columns)
W6 = pd.DataFrame(W6, columns = Xsp6.columns)

# Exogenous spatial lag models -- will be called by pysal later on

WXsp1 = pd.concat([Xsp1, W1], axis = 1)
WXsp2 = pd.concat([Xsp2, W2], axis = 1)
WXsp3 = pd.concat([Xsp3, W3], axis = 1)
WXsp4 = pd.concat([Xsp4, W4], axis = 1)
WXsp5 = pd.concat([Xsp5, W5], axis = 1)
WXsp6 = pd.concat([Xsp6, W6], axis = 1)

# Dataframes ready for baselines OLS regression

X1 = stats.add_constant(Xsp1)
X2 = stats.add_constant(Xsp2)
X3 = stats.add_constant(Xsp3)
X4 = stats.add_constant(Xsp4)
X5 = stats.add_constant(Xsp5)
X6 = stats.add_constant(Xsp6)

# Dataframes ready for spatial models

WX1 = stats.add_constant(WXsp1)
WX2 = stats.add_constant(WXsp2)
WX3 = stats.add_constant(WXsp3)
WX4 = stats.add_constant(WXsp4)
WX5 = stats.add_constant(WXsp5)
WX6 = stats.add_constant(WXsp6)

# Running OLS regression models

model1 = stats.OLS(Ysp, X1)
results1 = model1.fit()
print(results1.summary())
file = open('C:/Users/User/Documents/Data/MoF/model1.txt', 'w')
file.write(results1.summary().as_text())
file.close()

model2 = stats.OLS(Ysp, X2)
results2 = model2.fit()
print(results2.summary())
file = open('C:/Users/User/Documents/Data/MoF/model2.txt', 'w')
file.write(results2.summary().as_text())
file.close()

model3 = stats.OLS(Ysp, X3)
results3 = model3.fit()
print(results3.summary())
file = open('C:/Users/User/Documents/Data/MoF/model3.txt', 'w')
file.write(results3.summary().as_text())
file.close()

model4 = stats.OLS(Ysp, X4)
results4 = model4.fit()
print(results4.summary())
file = open('C:/Users/User/Documents/Data/MoF/model4.txt', 'w')
file.write(results4.summary().as_text())
file.close()

model5 = stats.OLS(Ysp, X5)
results5 = model5.fit()
print(results5.summary())
file = open('C:/Users/User/Documents/Data/MoF/model5.txt', 'w')
file.write(results5.summary().as_text())
file.close()

model6 = stats.OLS(Ysp, X6)
results6 = model6.fit()
print(results6.summary())
file = open('C:/Users/User/Documents/Data/MoF/model6.txt', 'w')
file.write(results6.summary().as_text())
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

sperror1 = pysal.model.spreg.ML_Error(Ysp.values[:,None], Xsp1.values, w = w, name_x = Xsp1.columns.tolist(), name_y = 'CO2 Intensity')
print(sperror1.summary)
file = open('C:/Users/User/Documents/Data/MoF/sperror1.txt', 'w')
file.write(sperror1.summary)
file.close()

sperror2 = pysal.model.spreg.ML_Error(Ysp.values[:,None], Xsp2.values, w = w, name_x = Xsp2.columns.tolist(), name_y = 'CO2 Intensity')
print(sperror2.summary)
file = open('C:/Users/User/Documents/Data/MoF/sperror2.txt', 'w')
file.write(sperror2.summary)
file.close()

sperror3 = pysal.model.spreg.ML_Error(Ysp.values[:,None], Xsp3.values, w = w, name_x = Xsp3.columns.tolist(), name_y = 'CO2 Intensity')
print(sperror3.summary)
file = open('C:/Users/User/Documents/Data/MoF/sperror3.txt', 'w')
file.write(sperror3.summary)
file.close()

sperror4 = pysal.model.spreg.ML_Error(Ysp.values[:,None], Xsp4.values, w = w, name_x = Xsp4.columns.tolist(), name_y = 'CO2 Intensity')
print(sperror4.summary)
file = open('C:/Users/User/Documents/Data/MoF/sperror4.txt', 'w')
file.write(sperror4.summary)
file.close()

sperror5 = pysal.model.spreg.ML_Error(Ysp.values[:,None], Xsp5.values, w = w, name_x = Xsp5.columns.tolist(), name_y = 'CO2 Intensity')
print(sperror5.summary)
file = open('C:/Users/User/Documents/Data/MoF/sperror5.txt', 'w')
file.write(sperror5.summary)
file.close()

sperror6 = pysal.model.spreg.ML_Error(Ysp.values[:,None], Xsp6.values, w = w, name_x = Xsp6.columns.tolist(), name_y = 'CO2 Intensity')
print(sperror6.summary)
file = open('C:/Users/User/Documents/Data/MoF/sperror6.txt', 'w')
file.write(sperror6.summary)
file.close()

# Running full spatial model in pysal

sp1 = pysal.model.spreg.ML_Lag(Ysp.values[:,None], Xsp1.values, w = w, name_x = Xsp1.columns.tolist(), name_y = 'CO2 Intensity')
print(sp1.summary)
file = open('C:/Users/User/Documents/Data/MoF/sp1.txt', 'w')
file.write(sp1.summary)
file.close()

sp2 = pysal.model.spreg.ML_Lag(Ysp.values[:,None], Xsp2.values, w = w, name_x = Xsp2.columns.tolist(), name_y = 'CO2 Intensity')
print(sp2.summary)
file = open('C:/Users/User/Documents/Data/MoF/sp2.txt', 'w')
file.write(sp2.summary)
file.close()

sp3 = pysal.model.spreg.ML_Lag(Ysp.values[:,None], Xsp3.values, w = w, name_x = Xsp3.columns.tolist(), name_y = 'CO2 Intensity')
print(sp3.summary)
file = open('C:/Users/User/Documents/Data/MoF/sp3.txt', 'w')
file.write(sp3.summary)
file.close()

sp4 = pysal.model.spreg.ML_Lag(Ysp.values[:,None], Xsp4.values, w = w, name_x = Xsp4.columns.tolist(), name_y = 'CO2 Intensity')
print(sp4.summary)
file = open('C:/Users/User/Documents/Data/MoF/sp4.txt', 'w')
file.write(sp4.summary)
file.close()

sp5 = pysal.model.spreg.ML_Lag(Ysp.values[:,None], Xsp5.values, w = w, name_x = Xsp5.columns.tolist(), name_y = 'CO2 Intensity')
print(sp5.summary)
file = open('C:/Users/User/Documents/Data/MoF/sp5.txt', 'w')
file.write(sp5.summary)
file.close()

sp6 = pysal.model.spreg.ML_Lag(Ysp.values[:,None], Xsp6.values, w = w, name_x = Xsp6.columns.tolist(), name_y = 'CO2 Intensity')
print(sp6.summary)
file = open('C:/Users/User/Documents/Data/MoF/sp6.txt', 'w')
file.write(sp6.summary)
file.close()

