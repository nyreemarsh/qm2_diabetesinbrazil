import pandas as pandas
import matplotlib
import pylab
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
pylab.rcParams['figure.figsize'] = (10., 10.)

plt.style.use('dark_background')

df = pandas.read_csv('Full Brazil America Dataset.csv')
df=df[df['metric']=='Number']
df=df[df['age']=='All ages']
print(df)

df['val_in_ht']=df['val']/100000
df_B = df[df['location']=='Brazil']

plt.figure(figsize=(8,6))

# plot line
plt.plot(df_B['year'], df_B['val_in_ht'],
         lw=2.5,
         color='#5DDEFB')
plt.scatter(df_B['year'], df_B['val_in_ht'],
            color='#B0ECF9')

# set label
plt.xlabel('Year')
plt.ylabel('Number of Incidences of Diabetes, in hundred thousands')

plt.title('Number of Incidences of Diabetes Over Time in Brazil')
plt.show()
