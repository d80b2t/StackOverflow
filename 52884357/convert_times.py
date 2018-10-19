
import pandas as pd
import numpy as np
from astropy.time import Time

#path     = '~/StackOverflow/52884357'
#df = pd.read_csv(path+filename)
filename = 'times.csv'
df = pd.read_csv(filename)

times = df['timestamp']

## THIS IS THE WRONG COMMAND::
#t = pd.Timestamp(times)

t = pd.to_datetime(times)
print(t)

