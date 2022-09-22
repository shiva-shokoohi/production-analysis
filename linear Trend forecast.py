# Production analysis
# Forecast calcuation - Linear Trend Forecast
# -----------------------------------------------------------
# By Shiva Shokoohi Mehran
# shiva.shokoohi.mehran@gmail.com
# summer 2022 - University of Windsor , CANADA
# -----------------------------------------------------------

import math
import matplotlib.pyplot as plt

def forecastCalcuation(actual):
  num = len(actual)
  x = range(1, num+1)
  xx = [] 
  yy = []
  xy = []
  f= []

  for inx,val in enumerate(actual):
    xx.append(x[inx] ** 2)
    yy.append(val**2)
    xy.append(x[inx] * val)

  k = ((num*sum(xx))-(sum(x)**2))*((num*sum(yy))-(sum(actual)**2))
  r = ((num*sum(xy))-(sum(x)*sum(actual)))/math.sqrt(k)
  alpha = ((sum(actual)*sum(xx))-(sum(x)*sum(xy)))/((num*sum(xx))-((sum(x))**2))
  beta = ((num*sum(xy))-(sum(x))*(sum(actual)))/(num*sum(xx)-((sum(x))**2))

  for i in range(0, len(x)):
    f.append(alpha+beta*x[i])

  return f

# TEST
inputs = [125,130,141,142,150,157,157,164,167,171]
forecast = forecastCalcuation(inputs)
print(forecast)

plt.plot(range(0,len(inputs)), inputs)
plt.plot(range(0,len(inputs)), forecast)
plt.show()
