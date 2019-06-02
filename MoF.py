# This script performs the statistical analysis for Molecules of Freedom

# For clarity, 'Molecules of Freedom' is an idiotic catchphrase used by the Trump
# administration to reference CO2 emissions specifically and GHG emissions generally.

# Importing required modules

import pandas as pd
import statsmodels.api as stats
import pysal

# Loading the data sets and storing them in dataframes

filepath = 'C:/Users/M535040/Documents/Data/MOF.csv'
filepath_rd = 'C:/Users/M535040/Documents/Data/MOF-R&D.csv'

data = pd.read_csv(filepath)
data_rd = pd.read_csv(filepath_rd)

# Creating dataframes for regression models

# Endogenous variables

GHG = data['GHG']
CO2 = data['CO2']
NOx = data['Nox']
CH4 = data['CH4']
GHG_cap = data['GHG-cap']
CO2_cap = data['CO2-cap']
NOx_cap = data['Nox-cap']
CH4_cap = data['CH4-cap']
CO2_intensity = data['CO2-Intensity']

GHG_rd = data_rd['GHG']
CO2_rd = data_rd['CO2']
NOx_rd = data_rd['Nox']
CH4_rd = data_rd['CH4']
GHG_cap_rd = data_rd['GHG-cap']
CO2_cap_rd = data_rd['CO2-cap']
NOx_cap_rd = data_rd['Nox-cap']
CH4_cap_rd = data_rd['CH4-cap']
CO2_intensity_rd = data_rd['CO2-Intensity']

# Exogenous variables

X_GHG_GDP = data[['GHG-lag', 'GDP', 'GDP2', 'Latitude', 'Renewable Energy', 'Polity Index', 'Tariff Rate']]
X_GHG_GDP = stats.add_constant(X_GHG_GDP)

X_GHG_GDP_rd = data_rd[['GHG-lag', 'GDP', 'GDP2', 'Latitude', 'Renewable Energy', 'R&D', 'Polity Index', 'Tariff Rate']]
X_GHG_GDP_rd = stats.add_constant(X_GHG_GDP_rd)

X_CO2_GDP = data[['CO2-lag', 'GDP', 'GDP2', 'Latitude', 'Renewable Energy', 'Polity Index', 'Tariff Rate']]
X_CO2_GDP = stats.add_constant(X_CO2_GDP)

X_CO2_GDP_rd = data_rd[['CO2-lag', 'GDP', 'GDP2', 'Latitude', 'Renewable Energy', 'R&D', 'Polity Index', 'Tariff Rate']]
X_CO2_GDP = stats.add_constant(X_CO2_GDP)

X_NOx_GDP = data[['Nox-lag', 'GDP', 'GDP2', 'Latitude', 'Renewable Energy', 'Polity Index', 'Tariff Rate']]
X_NOx_GDP = stats.add_constant(X_NOx_GDP)

X_NOx_GDP_rd = data_rd[['Nox-lag', 'GDP', 'GDP2', 'Latitude', 'Renewable Energy', 'R&D', 'Polity Index', 'Tariff Rate']]
X_NOx_GDP_rd = stats.add_constant(X_NOx_GDP_rd)

X_CH4_GDP = data[['CH4-lag', 'GDP', 'GDP2', 'Latitude', 'Renewable Energy', 'Polity Index', 'Tariff Rate']]
X_CH4_GDP = stats.add_constant(X_CH4_GDP)

X_CH4_GDP_rd = data_rd[['CH4-lag', 'GDP', 'GDP2', 'Latitude', 'Renewable Energy', 'R&D', 'Polity Index', 'Tariff Rate']]
X_CH4_GDP_rd = stats.add_constant(X_CH4_GDP_rd)

X_GHG_cap_GDP = data[['GHG-cap-lag', 'GDP', 'GDP2', 'Latitude', 'Renewable Energy', 'Polity Index', 'Tariff Rate']]
X_GHG_cap_GDP = stats.add_constant(X_GHG_cap_GDP)

X_GHG_cap_GDP_rd = data_rd[['GHG-cap-lag', 'GDP', 'GDP2', 'Latitude', 'Renewable Energy', 'R&D', 'Polity Index', 'Tariff Rate']]
X_GHG_cap_GDP_rd = stats.add_constant(X_GHG_cap_GDP_rd)

X_CO2_cap_GDP = data[['CO2-cap-lag', 'GDP', 'GDP2', 'Latitude', 'Renewable Energy', 'Polity Index', 'Tariff Rate']]
X_CO2_cap_GDP = stats.add_constant(X_CO2_cap_GDP)

X_CO2_cap_GDP_rd = data_rd[['CO2-cap-lag', 'GDP', 'GDP2', 'Latitude', 'Renewable Energy', 'R&D', 'Polity Index', 'Tariff Rate']]
X_CO2_cap_GDP_rd = stats.add_constant(X_CO2_cap_GDP_rd)

X_NOx_cap_GDP = data[['Nox-cap-lag', 'GDP', 'GDP2', 'Latitude', 'Renewable Energy', 'Polity Index', 'Tariff Rate']]
X_NOx_cap_GDP = stats.add_constant(X_NOx_cap_GDP)

X_NOx_cap_GDP_rd = data_rd[['Nox-cap-lag', 'GDP', 'GDP2', 'Latitude', 'Renewable Energy', 'R&D', 'Polity Index', 'Tariff Rate']]
X_NOx_cap_GDP_rd = stats.add_constant(X_NOx_GDP_rd)

X_CH4_cap_GDP = data[['CH4-cap-lag', 'GDP', 'GDP2', 'Latitude', 'Renewable Energy', 'Polity Index', 'Tariff Rate']]
X_CH4_cap_GDP = stats.add_constant(X_CH4_cap_GDP)

X_CH4_cap_GDP_rd = data_rd[['CH4-cap-lag', 'GDP', 'GDP2', 'Latitude', 'Renewable Energy', 'R&D', 'Polity Index', 'Tariff Rate']]
X_CH4_cap_GDP_rd = stats.add_constant(X_CH4_cap_GDP_rd)

X_CO2_int_GDP = data[['GDP', 'GDP2', 'Latitude', 'Renewable Energy', 'Polity Index', 'Tariff Rate']]
X_CO2_int_GDP = stats.add_constant(X_CO2_int_GDP)

X_CO2_int_GDP_rd = data_rd[['GDP', 'GDP2', 'Latitude', 'Renewable Energy', 'R&D', 'Polity Index', 'Tariff Rate']]
X_CO2_int_GDP_rd = stats.add_constant(X_CO2_int_GDP_rd)

X_GHG_PPP = data[['GHG-lag', 'GDP-PPP', 'GDP-PPP2', 'Latitude', 'Renewable Energy', 'Polity Index', 'Tariff Rate']]
X_GHG_PPP = stats.add_constant(X_GHG_PPP)

X_GHG_PPP_rd = data_rd[['GHG-lag', 'GDP-PPP', 'GDP-PPP2', 'Latitude', 'Renewable Energy', 'R&D', 'Polity Index', 'Tariff Rate']]
X_GHG_PPP_rd = stats.add_constant(X_GHG_PPP_rd)

X_CO2_PPP = data[['CO2-lag', 'GDP-PPP', 'GDP-PPP2', 'Latitude', 'Renewable Energy', 'Polity Index', 'Tariff Rate']]
X_CO2_PPP = stats.add_constant(X_CO2_PPP)

X_CO2_PPP_rd = data_rd[['CO2-lag', 'GDP-PPP', 'GDP-PPP2', 'Latitude', 'Renewable Energy', 'R&D', 'Polity Index', 'Tariff Rate']]
X_CO2_PPP_rd = stats.add_constant(X_CO2_PPP_rd)

X_NOx_PPP = data[['Nox-lag', 'GDP-PPP', 'GDP-PPP2', 'Latitude', 'Renewable Energy', 'Polity Index', 'Tariff Rate']]
X_NOx_PPP = stats.add_constant(X_NOx_PPP)

X_NOx_PPP_rd = data_rd[['Nox-lag', 'GDP-PPP', 'GDP-PPP2', 'Latitude', 'Renewable Energy', 'R&D', 'Polity Index', 'Tariff Rate']]
X_NOx_PPP_rd = stats.add_constant(X_NOx_PPP_rd)

X_CH4_PPP = data[['CH4-lag', 'GDP-PPP', 'GDP-PPP2', 'Latitude', 'Renewable Energy', 'Polity Index', 'Tariff Rate']]
X_CH4_PPP = stats.add_constant(X_CH4_PPP)

X_CH4_PPP_rd = data_rd[['CH4-lag', 'GDP-PPP', 'GDP-PPP2', 'Latitude', 'Renewable Energy', 'R&D', 'Polity Index', 'Tariff Rate']]
X_CH4_PPP_rd = stats.add_constant(X_CH4_PPP_rd)

X_GHG_cap_PPP = data[['GHG-cap-lag', 'GDP-PPP', 'GDP-PPP2', 'Latitude', 'Renewable Energy', 'Polity Index', 'Tariff Rate']]
X_GHG_cap_PPP = stats.add_constant(X_GHG_cap_PPP)

X_GHG_cap_PPP_rd = data_rd[['GHG-cap-lag', 'GDP-PPP', 'GDP-PPP2', 'Latitude', 'Renewable Energy', 'R&D', 'Polity Index', 'Tariff Rate']]
X_GHG_cap_PPP_rd = stats.add_constant(X_GHG_cap_PPP_rd)

X_CO2_cap_PPP = data[['CO2-cap-lag', 'GDP-PPP', 'GDP-PPP2', 'Latitude', 'Renewable Energy', 'Polity Index', 'Tariff Rate']]
X_CO2_cap_PPP = stats.add_constant(X_CO2_cap_PPP)

X_CO2_cap_PPP_rd = data_rd[['CO2-cap-lag', 'GDP-PPP', 'GDP-PPP2', 'Latitude', 'Renewable Energy', 'R&D', 'Polity Index', 'Tariff Rate']]
X_CO2_cap_PPP_rd = stats.add_constant(X_CO2_cap_PPP_rd)

X_NOx_cap_PPP = data[['Nox-cap-lag', 'GDP-PPP', 'GDP-PPP2', 'Latitude', 'Renewable Energy', 'Polity Index', 'Tariff Rate']]
X_NOx_cap_PPP = stats.add_constant(X_NOx_cap_PPP)

X_NOx_cap_PPP_rd = data_rd[['Nox-cap-lag', 'GDP-PPP', 'GDP-PPP2', 'Latitude', 'Renewable Energy', 'R&D', 'Polity Index', 'Tariff Rate']]
X_NOx_cap_PPP_rd = stats.add_constant(X_NOx_cap_PPP_rd)

X_CH4_cap_PPP = data[['CH4-cap-lag', 'GDP-PPP', 'GDP-PPP2', 'Latitude', 'Renewable Energy', 'Polity Index', 'Tariff Rate']]
X_CH4_cap_PPP = stats.add_constant(X_CH4_cap_PPP)

X_CH4_cap_PPP_rd = data_rd[['CH4-cap-lag', 'GDP-PPP', 'GDP-PPP2', 'Latitude', 'Renewable Energy', 'R&D', 'Polity Index', 'Tariff Rate']]
X_CH4_cap_PPP_rd = stats.add_constant(X_CH4_cap_PPP_rd)

X_CO2_int_PPP = data[['GDP-PPP', 'GDP-PPP2', 'Latitude', 'Renewable Energy', 'Polity Index', 'Tariff Rate']]
X_CO2_int_PPP = stats.add_constant(X_CO2_int_PPP)

X_CO2_int_PPP_rd = data_rd[['GDP-PPP', 'GDP-PPP2', 'Latitude', 'Renewable Energy', 'R&D', 'Polity Index', 'Tariff Rate']]
X_CO2_int_PPP_rd = stats.add_constant(X_CO2_int_PPP_rd)

# Running baseline AR1 autoregressive models

model = stats.OLS(GHG.astype(float), X_GHG_GDP.astype(float))
results = model.fit()
print(results.summary())
file = open('C:/Users/M535040/Documents/Data/MoF/GHG-GDP.txt', 'w')
file.write(results.summary().as_text())
file.close()

model = stats.OLS(GHG_rd.astype(float), X_GHG_GDP_rd.astype(float))
results = model.fit()
print(results.summary())
file = open('C:/Users/M535040/Documents/Data/MoF/GHG-GDP-rd.txt', 'w')
file.write(results.summary().as_text())
file.close()

model = stats.OLS(GHG_cap.astype(float), X_GHG_cap_GDP.astype(float))
results = model.fit()
print(results.summary())
file = open('C:/Users/M535040/Documents/Data/MoF/GHG-cap-GDP.txt', 'w')
file.write(results.summary().as_text())
file.close()

model = stats.OLS(GHG_cap_rd.astype(float), X_GHG_cap_GDP_rd.astype(float))
results = model.fit()
print(results.summary())
file = open('C:/Users/M535040/Documents/Data/MoF/GHG-cap-GDP-rd.txt', 'w')
file.write(results.summary().as_text())
file.close()

model = stats.OLS(CO2.astype(float), X_CO2_GDP.astype(float))
results = model.fit()
print(results.summary())
file = open('C:/Users/M535040/Documents/Data/MoF/CO2-GDP.txt', 'w')
file.write(results.summary().as_text())
file.close()

model = stats.OLS(CO2_rd.astype(float), X_CO2_GDP_rd.astype(float))
results = model.fit()
print(results.summary())
file = open('C:/Users/M535040/Documents/Data/MoF/CO2-GDP-rd.txt', 'w')
file.write(results.summary().as_text())
file.close()

model = stats.OLS(CO2_cap.astype(float), X_CO2_cap_GDP.astype(float))
results = model.fit()
print(results.summary())
file = open('C:/Users/M535040/Documents/Data/MoF/CO2-cap-GDP.txt', 'w')
file.write(results.summary().as_text())
file.close()

model = stats.OLS(CO2_cap_rd.astype(float), X_CO2_cap_GDP_rd.astype(float))
results = model.fit()
print(results.summary())
file = open('C:/Users/M535040/Documents/Data/MoF/CO2-cap-GDP-rd.txt', 'w')
file.write(results.summary().as_text())
file.close()

model = stats.OLS(CH4.astype(float), X_CH4_GDP.astype(float))
results = model.fit()
print(results.summary())
file = open('C:/Users/M535040/Documents/Data/MoF/CH4-GDP.txt', 'w')
file.write(results.summary().as_text())
file.close()

model = stats.OLS(CH4_rd.astype(float), X_CH4_GDP_rd.astype(float))
results = model.fit()
print(results.summary())
file = open('C:/Users/M535040/Documents/Data/MoF/CH4-GDP-rd.txt', 'w')
file.write(results.summary().as_text())
file.close()

model = stats.OLS(CH4_cap.astype(float), X_CH4_cap_GDP.astype(float))
results = model.fit()
print(results.summary())
file = open('C:/Users/M535040/Documents/Data/MoF/CH4-cap-GDP.txt', 'w')
file.write(results.summary().as_text())
file.close()

model = stats.OLS(CH4_cap_rd.astype(float), X_CH4_cap_GDP_rd.astype(float))
results = model.fit()
print(results.summary())
file = open('C:/Users/M535040/Documents/Data/MoF/CH4-cap-GDP-rd.txt', 'w')
file.write(results.summary().as_text())
file.close()

model = stats.OLS(NOx.astype(float), X_NOx_GDP.astype(float))
results = model.fit()
print(results.summary())
file = open('C:/Users/M535040/Documents/Data/MoF/NOx-GDP.txt', 'w')
file.write(results.summary().as_text())
file.close()

model = stats.OLS(NOx_rd.astype(float), X_NOx_GDP_rd.astype(float))
results = model.fit()
print(results.summary())
file = open('C:/Users/M535040/Documents/Data/MoF/NOx-GDP-rd.txt', 'w')
file.write(results.summary().as_text())
file.close()

model = stats.OLS(NOx_cap.astype(float), X_NOx_cap_GDP.astype(float))
results = model.fit()
print(results.summary())
file = open('C:/Users/M535040/Documents/Data/MoF/NOx-cap-GDP.txt', 'w')
file.write(results.summary().as_text())
file.close()

model = stats.OLS(NOx_cap_rd.astype(float), X_NOx_cap_GDP_rd.astype(float))
results = model.fit()
print(results.summary())
file = open('C:/Users/M535040/Documents/Data/MoF/NOx-cap-GDP-rd.txt', 'w')
file.write(results.summary().as_text())
file.close()

model = stats.OLS(CO2_intensity.astype(float), X_CO2_int_GDP.astype(float))
results = model.fit()
print(results.summary())
file = open('C:/Users/M535040/Documents/Data/MoF/CO2-int-GDP.txt', 'w')
file.write(results.summary().as_text())
file.close()

model = stats.OLS(CO2_intensity_rd.astype(float), X_CO2_int_GDP_rd.astype(float))
results = model.fit()
print(results.summary())
file = open('C:/Users/M535040/Documents/Data/MoF/CO2-int-GDP-rd.txt', 'w')
file.write(results.summary().as_text())
file.close()

model = stats.OLS(GHG.astype(float), X_GHG_PPP.astype(float))
results = model.fit()
print(results.summary())
file = open('C:/Users/M535040/Documents/Data/MoF/GHG-PPP.txt', 'w')
file.write(results.summary().as_text())
file.close()

model = stats.OLS(GHG_rd.astype(float), X_GHG_PPP_rd.astype(float))
results = model.fit()
print(results.summary())
file = open('C:/Users/M535040/Documents/Data/MoF/GHG-PPP-rd.txt', 'w')
file.write(results.summary().as_text())
file.close()

model = stats.OLS(GHG_cap.astype(float), X_GHG_cap_PPP.astype(float))
results = model.fit()
print(results.summary())
file = open('C:/Users/M535040/Documents/Data/MoF/GHG-cap-PPP.txt', 'w')
file.write(results.summary().as_text())
file.close()

model = stats.OLS(GHG_cap_rd.astype(float), X_GHG_cap_PPP_rd.astype(float))
results = model.fit()
print(results.summary())
file = open('C:/Users/M535040/Documents/Data/MoF/GHG-cap-PPP-rd.txt', 'w')
file.write(results.summary().as_text())
file.close()

model = stats.OLS(CO2.astype(float), X_CO2_PPP.astype(float))
results = model.fit()
print(results.summary())
file = open('C:/Users/M535040/Documents/Data/MoF/CO2-PPP.txt', 'w')
file.write(results.summary().as_text())
file.close()

model = stats.OLS(CO2_rd.astype(float), X_CO2_PPP_rd.astype(float))
results = model.fit()
print(results.summary())
file = open('C:/Users/M535040/Documents/Data/MoF/CO2-PPP-rd.txt', 'w')
file.write(results.summary().as_text())
file.close()

model = stats.OLS(CO2_cap.astype(float), X_CO2_cap_PPP.astype(float))
results = model.fit()
print(results.summary())
file = open('C:/Users/M535040/Documents/Data/MoF/CO2-cap-PPP.txt', 'w')
file.write(results.summary().as_text())
file.close()

model = stats.OLS(CO2_cap_rd.astype(float), X_CO2_cap_PPP_rd.astype(float))
results = model.fit()
print(results.summary())
file = open('C:/Users/M535040/Documents/Data/MoF/CO2-cap-PPP-rd.txt', 'w')
file.write(results.summary().as_text())
file.close()

model = stats.OLS(CH4.astype(float), X_CH4_PPP.astype(float))
results = model.fit()
print(results.summary())
file = open('C:/Users/M535040/Documents/Data/MoF/CH4-PPP.txt', 'w')
file.write(results.summary().as_text())
file.close()

model = stats.OLS(CH4_rd.astype(float), X_CH4_PPP_rd.astype(float))
results = model.fit()
print(results.summary())
file = open('C:/Users/M535040/Documents/Data/MoF/CH4-PPP-rd.txt', 'w')
file.write(results.summary().as_text())
file.close()

model = stats.OLS(CH4_cap.astype(float), X_CH4_cap_PPP.astype(float))
results = model.fit()
print(results.summary())
file = open('C:/Users/M535040/Documents/Data/MoF/CH4-cap-PPP.txt', 'w')
file.write(results.summary().as_text())
file.close()

model = stats.OLS(CH4_cap_rd.astype(float), X_CH4_cap_PPP_rd.astype(float))
results = model.fit()
print(results.summary())
file = open('C:/Users/M535040/Documents/Data/MoF/CH4-cap-PPP-rd.txt', 'w')
file.write(results.summary().as_text())
file.close()

model = stats.OLS(NOx.astype(float), X_NOx_PPP.astype(float))
results = model.fit()
print(results.summary())
file = open('C:/Users/M535040/Documents/Data/MoF/NOx-PPP.txt', 'w')
file.write(results.summary().as_text())
file.close()

model = stats.OLS(NOx_rd.astype(float), X_NOx_PPP_rd.astype(float))
results = model.fit()
print(results.summary())
file = open('C:/Users/M535040/Documents/Data/MoF/NOx-PPP-rd.txt', 'w')
file.write(results.summary().as_text())
file.close()

model = stats.OLS(NOx_cap.astype(float), X_NOx_cap_PPP.astype(float))
results = model.fit()
print(results.summary())
file = open('C:/Users/M535040/Documents/Data/MoF/NOx-cap-PPP.txt', 'w')
file.write(results.summary().as_text())
file.close()

model = stats.OLS(NOx_cap_rd.astype(float), X_NOx_cap_PPP_rd.astype(float))
results = model.fit()
print(results.summary())
file = open('C:/Users/M535040/Documents/Data/MoF/NOx-cap-PPP-rd.txt', 'w')
file.write(results.summary().as_text())
file.close()

model = stats.OLS(CO2_intensity.astype(float), X_CO2_int_PPP.astype(float))
results = model.fit()
print(results.summary())
file = open('C:/Users/M535040/Documents/Data/MoF/CO2-int-PPP.txt', 'w')
file.write(results.summary().as_text())
file.close()

model = stats.OLS(CO2_intensity_rd.astype(float), X_CO2_int_PPP_rd.astype(float))
results = model.fit()
print(results.summary())
file = open('C:/Users/M535040/Documents/Data/MoF/CO2-int-PPP-rd.txt', 'w')
file.write(results.summary().as_text())
file.close()

# Repeating these analyses with a spatial error model using pysal
















