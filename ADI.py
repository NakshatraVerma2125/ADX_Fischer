#Importing Packages
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Loading the data
df = pd.read_csv('Task1.csv')




lookback=14#Setting the lookback period to its traditional setting of 14

# Finding the ATR
TR_P1 = df['High'] - df['Low']
TR_P2 = abs(df['High'] - df['Close'].shift(1))
TR_P3= abs(df['Low'] - df['Close'].shift(1))
TR_possibilties = [TR_P1, TR_P2, TR_P3]
TR = pd.concat(TR_possibilties, axis = 1).max(axis = 1)
Avg_TR = TR.rolling(lookback).mean()

# Finding plus_DM and minus_DM
plus_DM=df['High'].diff()
minus_DM=df['Low'].diff()


plus_DM[plus_DM < 0] = 0
minus_DM[minus_DM > 0] = 0

# Finding the plus_DI,minus_DI,ADX using standard formulas
df['Plus_DI'] = 100 * (plus_DM.ewm(alpha = 1/lookback).mean() / Avg_TR)
df['Minus_DI'] = abs(100 * (minus_DM.ewm(alpha = 1/lookback).mean() / Avg_TR))
di = (abs(df['Plus_DI'] - df['Minus_DI']) / abs(df['Plus_DI'] + df['Minus_DI'])) * 100
ADX = ((di.shift(1) * (lookback - 1)) + di) / lookback
df['ADX'] = ADX.ewm(alpha = 1/lookback).mean()

df = df.dropna()
print(df)
# Saving the csv file
df.to_csv('Modified csv(ADX).csv', index = False)


# Plotting the Graphs
df.plot(x='Date', y='Close',label = 'Closing Price')
plt.plot(df['Plus_DI'], color = 'r', label = '+ DI 14',alpha = 0.3)
plt.plot(df['Minus_DI'], color = 'g', label = '- DI 14', alpha = 0.3)
plt.plot(df['ADX'], color = 'k', label = 'ADX 14')
plt.legend()
plt.show()
