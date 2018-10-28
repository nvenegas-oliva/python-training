
import pandas as pd
import numpy as np
from datetime import datetime

import matplotlib.pyplot as plt
from matplotlib.pylab import rcParams
from statsmodels.tsa.stattools import adfuller
rcParams['figure.figsize'] = 15, 6

%matplotlib inline


df = pd.read_csv('time-series-forecasting/AirPassengers.csv')
df.head()

df.rename(columns={'#Passengers': 'Passengers'}, inplace=True)
df.info()

df['Month'] = pd.to_datetime(df['Month'])
df.set_index('Month', inplace=True)
df.head()

df.loc['1950']

df.loc[datetime(1950, 1, 1): datetime(1950, 12, 1)]

df.loc[datetime(1955, 1, 1):]


_ = df.plot()


def test_stationarity(timeseries):

    # Determing rolling statistics
    rolmean = timeseries.rolling(window=12).mean()
    rolstd = timeseries.rolling(window=12).std()

    # Plot rolling statistics:
    orig = plt.plot(timeseries, color='blue', label='Original')
    mean = plt.plot(rolmean, color='red', label='Rolling Mean')
    std = plt.plot(rolstd, color='black', label='Rolling Std')
    plt.legend(loc='best')
    plt.title('Rolling Mean & Standard Deviation')
    plt.show(block=False)

    # Perform Dickey-Fuller test:
    print('Results of Dickey-Fuller Test:')
    dftest = adfuller(timeseries, autolag='AIC')
    dfoutput = pd.Series(dftest[0:4],
                         index=['Test Statistic', 'p-value', '#Lags Used', 'Number of Observations Used'])
    for key, value in dftest[4].items():
        dfoutput['Critical Value (%s)' % key] = value
    print(dfoutput)


test_stationarity(df['Passengers'])
