import pandas as pd
import matplotlib.pyplot as plt

path = 'https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/DA0101EN/automobileEDA.csv'
df = pd.read_csv(path)
df.head()
df.hist(column='price', by='drive-wheels', bins=20)
df[['bore', 'stroke']].plot(kind='hist',
                            alpha=0.7,
                            bins=30,
                            title='Histogram Of Bore and Stroke in Engine',
                            rot=45,
                            grid=True,
                            figsize=(12, 8),
                            fontsize=15,
                            color=['#FF5733', '#5C33FF'])
plt.xlabel('Size')
plt.ylabel('Number of Cars')