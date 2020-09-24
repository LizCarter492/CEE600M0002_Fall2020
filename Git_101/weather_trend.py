#reads in NOAA daily weather values
#generates linear trend in TAVG
#prints model results to "results.txt"
#Writen by Elizabeth Carter, ekcarter@syr.edu, 9/13/2020

import pandas as pd
import numpy as np
from statsmodels.api import OLS

#Read in weather data included in git repository
weather_dat=pd.read_csv("2281205.csv")

#create np.array  representing accumulation of days
X = np.array(range(weather_dat.shape[0]))

#extract variable that we want to "predict"
Y = np.array(weather_dat.TMAX)

#THIS LINE IS NONSENSE...or is it? you decide if it should stay or go

#remove no data values
X=X[np.logical_not(np.isnan(Y))]
Y=Y[np.logical_not(np.isnan(Y))]

#calculate results of ordinary least squares regression
results =OLS(Y,X).fit().summary()

#open text file and save model results
text_file = open("results.txt", "w")
text_file.write(str(results))
text_file.close()
