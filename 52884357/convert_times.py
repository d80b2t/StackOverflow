
import pandas as pd
import numpy as np
from astropy.time import Time

path     = '~/StackOverflow/52884357'
filename = 'times.csv'
df = pd.read_csv(path+filename)

times = df['timestamp']


t = pd.Timestamp(times)


