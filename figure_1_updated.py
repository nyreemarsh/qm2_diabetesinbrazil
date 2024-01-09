import pandas as pandas
import matplotlib
import pylab
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
pylab.rcParams['figure.figsize'] = (10., 10.)

plt.style.use('dark_background')

df = pandas.read_csv('brazil_diabetes_fulldata.csv')
print(df)

df['val_percent']=df['val']*100

plt.figure(figsize=(8,6))

# plot line
plt.plot(df['year'], df['val_percent'],
         lw=2.5,
         color='#5DDEFB')
plt.scatter(df['year'], df['val_percent'],
            color='#B0ECF9')

# set label
plt.xlabel('Year')
plt.ylabel('Diabetes Prevalence %')

plt.title('Diabetes Prevalence Over Time in Brazil (as a percentage)')
plt.show()