
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


# Estimating and eliminating trend

_ = np.log(df['Passengers']).plot()


"""
In this simpler case, it is easy to see a forward trend in the data.
But its not very intuitive in presence of noise. So we can use some techniques
to estimate or model this trend and then remove it from the series.
There can be many ways of doing it and some of most commonly used are:

Aggregation – taking average for a time period like monthly/weekly averages
Smoothing – taking rolling averages
Polynomial Fitting – fit a regression model

In this approach, we take average of ‘k’ consecutive values depending on the
frequency of time series. Here we can take the average over the past 1 year,
i.e. last 12 values. Pandas has specific functions defined for
determining rolling statistics.
"""

ts_log = np.log(df['Passengers'])
moving_avg = ts_log.rolling(window=12).mean()
_ = np.log(df['Passengers']).plot()
_ = moving_avg.plot(color='red')


ts_log_moving_avg_diff = ts_log - moving_avg
ts_log_moving_avg_diff.head(12)

ts_log_moving_avg_diff.dropna(inplace=True)
test_stationarity(ts_log_moving_avg_diff)


"""
This looks like a much better series. The rolling values appear to be varying
slightly but there is no specific trend. Also, the test statistic is
smaller than the 5% critical values so we can say with 95% confidence
that this is a stationary series.
"""
expwighted_avg = ts_log.ewm(halflife=12)
_ = ts_log.plot()
_ = expwighted_avg.mean().plot(color='red')

"""
Note that here the parameter ‘halflife’ is used to define the amount of
exponential decay. This is just an assumption here and would depend
largely on the business domain. Other parameters like span and center of
mass can also be used to define decay which are discussed in the link shared
above. Now, let’s remove this from series and check stationarity:
"""


ts_log_ewma_diff = ts_log - expwighted_avg.mean()
test_stationarity(ts_log_ewma_diff)
