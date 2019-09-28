import pandas as pd
import matplotlib.pyplot as plt

url = "https://storage.googleapis.com/learn_pd_like_tidyverse/gapminder.csv"
dataInput = pd.read_csv(csv_url)

# review the dimension of data source
print(dataInput.shape)
dataInput.head

# GDP per capita and lifeExp - High Income Countries
uk = dataInput[dataInput['country'] == 'United Kingdom']
us = dataInput[dataInput['country'] == 'United States']
gn = dataInput[dataInput['country'] == 'Germany']

plt.plot(uk['gdpPercap'], uk['lifeExp'], label = 'United Kingdom')
plt.plot(us['gdpPercap'], us['lifeExp'], label = 'United States')
plt.plot(gn['gdpPercap'], gn['lifeExp'], label = 'Germany')
plt.title("GDP per Capita and lifeExp - High Income Countries ")
plt.xlabel('gpdPercap')
plt.ylabel('Life Expectancy')

plt.legend()
plt.show()

#GDP per capita and lifeExp - Middle Income Countries

ph = dataInput[dataInput['country'] == 'Philippines']
vn = dataInput[dataInput['country'] == 'Vietnam']
th = dataInput[dataInput['country'] == 'Thailand']

plt.plot(ph['gdpPercap'], ph['lifeExp'], label = 'Philippines')
plt.plot(vn['gdpPercap'], vn['lifeExp'], label = 'Vietnam')
plt.plot(th['gdpPercap'], th['lifeExp'], label = 'Thailand')
plt.title("GDP per Capita and lifeExp - Middle Income Countries ")
plt.xlabel('gpdPercap')
plt.ylabel('Life expectancy')

plt.legend()
plt.show()

#GDP per capita and lifeExp - Low Income Countries
cd = dataInput[dataInput['country'] == 'Chad']
sd = dataInput[dataInput['country'] == 'Sudan']
ug = dataInput[dataInput['country'] == 'Uganda']

plt.plot(cd['gdpPercap'], cd['lifeExp'], label = 'Chad')
plt.plot(sd['gdpPercap'], sd['lifeExp'], label = 'Sudan')
plt.plot(ug['gdpPercap'], ug['lifeExp'], label = 'Uganda')
plt.title("GDP per Capita and lifeExp - Low Income Countries ")
plt.xlabel('GDP per Capita')
plt.ylabel('Life expectancy')

plt.legend()
plt.show()

#GDP per capita and Life Expectancy - Five continents
fig, axes = plt.subplots(2, 3, figsize=(25, 12))
continents = dataInput["continent"].unique()
row_indices = [0, 0, 0, 1, 1]
col_indices = [0, 1, 2, 0, 1]
for conts, row_i, col_i in zip(continents, row_indices, col_indices):
    x = dataInput[dataInput["continent"] == conts]["gdpPercap"].values
    y = dataInput[dataInput["continent"] == conts]["lifeExp"].values
    axes[row_i,col_i].scatter(x,y,color= "gold")
    axes[row_i,col_i].set_title("{}".format(conts), fontsize=12)
    axes[1,2].set_visible(False)
plt.ylabel('Life expectancy')
fig.suptitle('GDP per Capita and Life Expectancy - Five continents', fontsize=14)
plt.show()
