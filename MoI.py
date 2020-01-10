# This script performs the statistical analysis for Molecules of Freedom'

# Importing required modules

import pandas as pd
import statsmodels.api as stats
import pysal
import geopandas as gpd
import matplotlib.pyplot as plt

# Loading the data ses and storing it in a dataframe

spatial_filepath = 'C:/Users/User/Documents/Data/MOI.csv'
sw_filepath = 'C:/Users/User/Documents/Data/MOI_W.csv'
mapdata_filepath = 'C:/Users/User/Documents/Data/MoImAp.csv'
shpath = 'C:/Users/User/Documents/Data/countries.shp'
plotsdatapath = 'C:/Users/User/Documents/Data/MoIplotsdata.csv'

spdata = pd.read_csv(spatial_filepath)
SW = pd.read_csv(sw_filepath, header = None)
mapdat = pd.read_csv(mapdata_filepath)
shpdat = gpd.read_file(shpath)
plotsdata = pd.read_csv(plotsdatapath)

# Creating dataframes for all regression models

# Endogenous variables

Y = spdata['Intensity']
Y2 = spdata['CO2']

# Exogenous variables

# Exogenous variables for spatial models -- will be called by pysal later on

Xsp1 = spdata[['Intensity_Lag', 'GDP', 'Renewable Energy', 'Coal Rents', 'Oil Rents', 'Crude Price', 'R&D', 'Tariff Rate']]
Xsp2 = spdata[['Intensity_Lag', 'GDP', 'Renewable Energy', 'Coal Rents', 'Oil Rents', 'Crude Price', 'R&D', 'Target Tariff']]
Xsp3 = spdata[['CO2_Lag', 'GDP', 'Renewable Energy', 'Coal Rents', 'Oil Rents', 'Crude Price', 'R&D', 'Tariff Rate']]
Xsp4 = spdata[['CO2_Lag', 'GDP', 'Renewable Energy', 'Coal Rents', 'Oil Rents', 'Crude Price', 'R&D', 'Target Tariff']]

# Dataframes ready for baseline OLS regression

X1 = stats.add_constant(Xsp1)
X2 = stats.add_constant(Xsp2)
X3 = stats.add_constant(Xsp3)
X4 = stats.add_constant(Xsp4)

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

model3 = stats.OLS(Y2, X3)
results3 = model3.fit()
print(results3.summary())
file = open('C:/Users/User/Documents/Data/MoF/model3.txt', 'w')
file.write(results3.summary().as_text())
file.close()

model4 = stats.OLS(Y2, X4)
results4 = model4.fit()
print(results4.summary())
file = open('C:/Users/User/Documents/Data/MoF/model4.txt', 'w')
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

sp3 = pysal.model.spreg.ML_Lag(Y2.values[:,None], Xsp3.values, w = w, name_x = Xsp3.columns.tolist(), name_y = 'CO2 per capita')
print(sp3.summary)
file = open('C:/Users/User/Documents/Data/MoF/splag3.txt', 'w')
file.write(sp3.summary)
file.close()

sp4 = pysal.model.spreg.ML_Lag(Y2.values[:,None], Xsp4.values, w = w, name_x = Xsp4.columns.tolist(), name_y = 'CO2 per capita')
print(sp4.summary)
file = open('C:/Users/User/Documents/Data/MoF/splag4.txt', 'w')
file.write(sp4.summary)
file.close()

# Creating choropleths for tariff rates and carbon intensities

# Blending the data and shape files

shpdat = shpdat[['COUNTRY', 'geometry']]
merged = shpdat.set_index('COUNTRY').join(mapdat.set_index('Country'))

# Creating a reference dictionary for looping choropleth creation and additional map parameters

vals = [str(mapdat.columns[i]) for i in range(1,len(mapdat.columns))]
titles = ['Carbon Intensities - 2012', 'Carbon Intensities - 1996', 'Mean Tariff Rates - 2012', 'Mean Tariff Rates - 1996',
          'CO2 Emissions per capita - 2012', 'CO2 Emissions per capita - 1996']
dic = dict(zip(vals, titles))
cols = ['Purples', 'Reds', 'Purples', 'Reds', 'Purples', 'Reds']

# Creating and saving the choropleths

for val, tit in dic.items():
    
    print('Creating choropleth for ' + tit + '\n')
    idx = vals.index(val)
    fig, ax = plt.subplots(1, figsize = (12,6))
    plt.axis('off')
    merged.plot(color = 'lightgray', linewidth = 0.5, ax = ax, edgecolor = '0.8', legend = False)
    plotdata = merged[['geometry', val]].dropna()
    plotdata.plot(column = val, cmap = cols[idx], linewidth = 0.5, ax = ax, edgecolor = '0.8', legend = True)
    plt.title(tit, fontsize = 14, fontweight = 40)
    plt.savefig('C:/Users/User/Documents/Data/MoF/' + val + '.png')

# Creating time series plots of CO2 intensities and CO2 emissions per capita for select countries

plots = ['CO2', 'Intensity']
nations = ['Canada', 'China', 'Russia', 'United Kingdom', 'United States']
cm = plt.get_cmap('gist_rainbow')
labels = ['CO2 Emissions (metric tons per capita)', 'Carbon Intensity (kg/USD)']
titles = ['Trends in per capita CO2 emissions: 1996 - 2012', 'Trends in carbon intensities: 1996 - 2012']
ylims = [[0,22],[0,2.5]]
codes = ['-', '--', '-.', ':', 'D']

for plot in plots:
    
    plt.figure()
    
    for nation in nations:
        
        d = plotsdata[plotsdata['Country'] == nation]
        plt.plot(d.Year, d[plot], codes[nations.index(nation)], label = nation, color = cm(nations.index(nation)/len(nations)))

    plt.title(titles[plots.index(plot)], loc = 'center', fontsize = 12, fontweight = 40, color = 'black')
    plt.ylim(ylims[plots.index(plot)])
    plt.ylabel(labels[plots.index(plot)])
    lgd = plt.legend(loc = 'upper center', bbox_to_anchor = (1.2, 0.8), shadow = True, ncol = 1)
    plt.savefig('C:/Users/User/Documents/Data/MoF/' + plot + '.eps', bbox_extra_artists = (lgd,), bbox_inches = 'tight')

