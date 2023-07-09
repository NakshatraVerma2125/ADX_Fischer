#Importing Packages
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Loading the csv file
df = pd.read_csv('Task1.csv')
#Normalizing the adjacent close to values between +1 and -1
min_adjclose = df['Adj Close'].min()
max_adjclose = df['Adj Close'].max()
df['x_normalized'] = 2*(df['Adj Close'] - min_adjclose)/(max_adjclose - min_adjclose) - 1

# Changing all +1's an-1's to 0.999 and -0.999 to avoid infinite values
df.loc[df['x_normalized'] == 1 , 'x_normalized'] = 0.999
df.loc[df['x_normalized'] == -1 , 'x_normalized'] = -0.999

# Finally Calculating the Fischer Transformation through the formula 
df['Fischer_Transformation'] = 0.5*(np.log((1.00+df['x_normalized'])/(1.00-df['x_normalized'])))
print(df)

# Saving the csv file
df.to_csv('Modified csv(Fischer Transformation).csv')

# Plotting the Graph
df.plot(x='Date', y='Fischer_Transformation')
plt.title('Fischer Transformation of Adj Closing Price')
plt.show()
