# Production analysis
# Forecast calcuation - Exponential Smoothing forecast
# -----------------------------------------------------------
# By Shiva Shokoohi Mehran
# shiva.shokoohi.mehran@gmail.com
# summer 2022 - University of Windsor , CANADA
# -----------------------------------------------------------

import matplotlib.pyplot as plt

def forecastCalcuation(a):
  alpha=float(input("please enter the alpha "))
  num=len(a)
  x=range(0,num)
  f=[]
  f.append(0)
  f.append(a[0])
  for i in range(2,len(a)+1):
    f.append(f[i-1]+alpha*(a[i-1]-f[i-1]))
  return f

# TEST
inputs = [125,130,141,142,150,157,157,164,167,171]
forecast = forecastCalcuation(inputs)
print(forecast)


plt.plot(range(0,len(inputs)), inputs)
plt.plot(range(1,len(inputs)+1), forecast[1:])
plt.show()





 