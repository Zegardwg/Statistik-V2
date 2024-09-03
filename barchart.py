import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

countries = ('Argentina','Bolivia','Brazil','Chile','Colombia','Ecuador',
            'Falkland Island','French Guiana','Guyana','Paraguay','Peru',
            'Suriname','Uruguay','Venezuela')

populations = (45076074, 11662410, 212162757, 19109629, 50818926, 17579085, 3481,
              287750, 785409, 7170305, 32880332, 585169, 3470475, 28258770)

df = pd.DataFrame({'Country': countries, 'Population': populations})
df.sort_values(by='Population', inplace=True)

x_coords = np.arange(len(df))
colors = ['#0000FF' for _ in range(len(df))]
colors[-2] = '#FF0000'

plt.bar(x_coords, df['Population'], tick_label=df['Country'], color=colors)
plt.xticks(rotation=90)
plt.ylabel('Population (Millions)')
plt.title('South American Countries Population')
plt.show()
