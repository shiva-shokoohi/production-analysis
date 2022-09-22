# Production analysis
# Forecast calcuation -Trend-adjusted Exponential Smoothing forecast
# -----------------------------------------------------------
# By Shiva Shokoohi Mehran
# shiva.shokoohi.mehran@gmail.com
# summer 2022 - University of Windsor , CANADA
# -----------------------------------------------------------

import matplotlib.pyplot as plt
import random as r

def forecastCalcuation(alpha,beta,r):
  x=range(1,len(r))
  t=[]
  taf=[]
  s=[]
  t = [0]*4
  taf=[0]*4
  s=[0]*4
  t.append((r[3]-r[0]) / 3)
  taf.append(r[3]+t[4])
  s.append(taf[4]+alpha*(r[4]-taf[4]))
  
  for i in range(5,len(x)+1):
    taf.append(s[i-1]+t[i-1])
    s.append(taf[i]+alpha*(r[i]-taf[i]))
    t.append(t[i-1]+beta*(taf[i]-taf[i-1]-t[i-1]))

  taf.append(s[-1]+t[-1])
  return taf

def rnd(firstNumber,count,threshold):
  col=[firstNumber]
  for i in range(0,count):
    col.append(col[-1]+r.randint(-threshold,threshold))
  return col

r=rnd(125,100,30)
forecast = forecastCalcuation(0.3,0.2,r)

plt.plot(range(0,len(r)), r)
plt.plot(range(4,len(r)+1), forecast[4:])
plt.show()