# This script performs the statistical analysis for Molecules of Freedom

# For clarity, 'Molecules of Freedom' is an idiotic catchphrase used by the 45th administration to reference natural gas

# Importing required modules

import pandas as pd
import statsmodels.api as stats

# Loading the data ses and storing it in a dataframe

filepath = 'C:/Users/User/Documents/Data/MOF-R&D.csv'

data = pd.read_csv(filepath)

# Creating dataframes for regression models

# Endogenous variables - CO2 intensity

CO2_intensity = data['CO2-Intensity']

# Exogenous variables - CO2 intensity

X_CO2_intensity = data[['GDP', 'GDP2', 'Renewable Energy', 'R&D', 'Tariff Rate']]
X_CO2_intensity = stats.add_constant(X_CO2_intensity)

X_CO2_intensity_pi = data[['GDP', 'GDP2', 'Renewable Energy', 'R&D', 'Tariff Rate', 'Polity Index']]
X_CO2_intensity_pi = stats.add_constant(X_CO2_intensity_pi)

X_CO2_intensity_lag = data[['CO2-Intense-lag', 'GDP', 'GDP2', 'Renewable Energy', 'R&D', 'Tariff Rate']]
X_CO2_intensity_lag = stats.add_constant(X_CO2_intensity_lag)

X_CO2_intensity_pi_lag = data[['CO2-Intense-lag', 'GDP', 'GDP2', 'Renewable Energy', 'R&D', 'Tariff Rate', 'Polity Index']]
X_CO2_intensity_pi_lag = stats.add_constant(X_CO2_intensity_pi_lag)

# Running the OLS models

model1 = stats.OLS(CO2_intensity, X_CO2_intensity)
results1 = model1.fit()
print(results1.summary())
file = open('C:/Users/User/Documents/Data/MoF/model1.txt', 'w')
file.write(results1.summary().as_text())
file.close()

model2 = stats.OLS(CO2_intensity, X_CO2_intensity_pi)
results2 = model2.fit()
print(results2.summary())
file = open('C:/Users/User/Documents/Data/MoF/model2.txt', 'w')
file.write(results2.summary().as_text())
file.close()


model3 = stats.OLS(CO2_intensity, X_CO2_intensity_lag)
results3 = model3.fit()
print(results3.summary())
file = open('C:/Users/User/Documents/Data/MoF/model3.txt', 'w')
file.write(results3.summary().as_text())
file.close()

model4 = stats.OLS(CO2_intensity, X_CO2_intensity_pi_lag)
results4 = model4.fit()
print(results4.summary())
file = open('C:/Users/User/Documents/Data/MoF/model4.txt', 'w')
file.write(results4.summary().as_text())
file.close()

##############################################################################

# Repeating above without GDP2 term as alternative to EKC hypothesis

# Exogenous variables - CO2 intensity

X_CO2_intensity = data[['GDP', 'Renewable Energy', 'R&D', 'Tariff Rate']]
X_CO2_intensity = stats.add_constant(X_CO2_intensity)

X_CO2_intensity_pi_rd = data[['GDP', 'Renewable Energy', 'R&D', 'Tariff Rate', 'Polity Index']]
X_CO2_intensity_pi_rd = stats.add_constant(X_CO2_intensity_pi_rd)

X_CO2_intensity_lag = data[['CO2-Intense-lag', 'GDP', 'Renewable Energy', 'R&D', 'Tariff Rate']]
X_CO2_intensity_lag = stats.add_constant(X_CO2_intensity_lag)

X_CO2_intensity_pi_rd_lag = data[['CO2-Intense-lag', 'GDP', 'Renewable Energy', 'R&D', 'Tariff Rate', 'Polity Index']]
X_CO2_intensity_pi_rd_lag = stats.add_constant(X_CO2_intensity_pi_rd_lag)

# Running the OLS alternatives

alternative1 = stats.OLS(CO2_intensity, X_CO2_intensity)
results1 = alternative1.fit()
print(results1.summary())
file = open('C:/Users/User/Documents/Data/MoF/alternative1.txt', 'w')
file.write(results1.summary().as_text())
file.close()

alternative2 = stats.OLS(CO2_intensity, X_CO2_intensity_pi)
results2 = alternative2.fit()
print(results2.summary())
file = open('C:/Users/User/Documents/Data/MoF/alternative2.txt', 'w')
file.write(results2.summary().as_text())
file.close()

alternative3 = stats.OLS(CO2_intensity, X_CO2_intensity_lag)
results3 = alternative3.fit()
print(results3.summary())
file = open('C:/Users/User/Documents/Data/MoF/alternative3.txt', 'w')
file.write(results3.summary().as_text())
file.close()

alternative4 = stats.OLS(CO2_intensity, X_CO2_intensity_pi_lag)
results4 = alternative4.fit()
print(results4.summary())
file = open('C:/Users/User/Documents/Data/MoF/alternative4.txt', 'w')
file.write(results4.summary().as_text())
file.close()

