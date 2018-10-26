
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

%matplotlib inline
sns.set()

pd.read_csv('time-series/appl_1980_2014.csv').head()

df = pd.read_csv('time-series/appl_1980_2014.csv', parse_dates=['Date'], index_col='Date')
df.info()


df.resample('BM').count()

df.index.max() - df.index.min()
(df.index.max() - df.index.min()).days


len(df.resample('M').count().index)


_ = plt.figure(figsize=(18, 6))
_ = df['Adj Close'].plot()
