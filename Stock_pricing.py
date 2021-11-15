
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns

from datetime import datetime
from sklearn.preprocessing import MinMaxScaler

from keras.models import Sequential
from keras.layers import Dense, LSTM

import warnings
warnings.filterwarnings('ignore')


# Set up End and Start times for data grab
end = datetime.now()
start = datetime(end.year - 1, end.month, end.day)

VCB = pd.read_csv('excel_vcb.csv',sep=',')
TCB = pd.read_csv('excel_tcb.csv',sep=',')
CTG = pd.read_csv('excel_ctg.csv',sep=',')

# VCB
Cols = ['Ticker','Date','Open','High','Low','Close','Volume']

VCB.columns = Cols

VCB['Date']=pd.to_datetime(VCB['Date'], format='%Y%m%d', errors='ignore')

VCB = VCB.sort_values(by='Date')

VCB = VCB.set_index(['Date'])
                         