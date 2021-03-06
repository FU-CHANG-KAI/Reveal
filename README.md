# Reveal
Reveal is a function which **visually displays the relation between economic growth (gdpPercapita) and life expectancy(lifeExp)** of specific continents and country groups


## Installation
Use pandas and matplotlib


## Usage

```python
import pandas as pd
import matplotlib.pyplot as plt

plt.plot # Line Plot
plt.boxplot # box plot
plt.subplots # Sub Plot
```

## Limitation
Reveal is still under construction. More features will be presented in the near feature.


## Observation

![](images/five%20continents.png)
FG.1 Sub plot

(1)In Asia, we can observe that life expectancy expoentially increases with the growth of GDP. 

(2)In Americas and Europe, life expectancy expoentially increeases with the growth of GDP anf then begin to linearly grow up. 

(3)But in Africa, even GDP per capita is in the same level, there are big differences between life expectancies.


<img src="images/box%20plot.png" width="400">

FG.2 Box plot

(1)Accoring to box plot, GDP per capita is extremely low and almost all people living in such poverty condition at Africa countries. 

(2)Further observations might be displayed by looking more detail at the below three charts.  



<img src="images/High%20Income.png" width="400">

FG.3 Line plot for high income countries

(1)Life expectancy linearly increases with the growth of GDP. 




<img src="images/Middle%20Income.png" width="400">

FG.4 Line plot for middle income countries

(1)Life expectancy expoentially increases with the growth of GDP. 



<img src="images/Low%20Income.png" width="400">

FG.5 Line plot for low income countries

(1)life expectancy does not relevant when GDP grows, which implies there are more essential factor effect human's lives in these areas. 


## Source of data
https://www.gapminder.org/

## Contributing
Note that the kit is still under construction. Pull requests are welcome. 
For major changes, please contact me via the mail alexreadbible@gmail.com.
