import numpy as np
import pandas as pd
# import warnings; warnings.simplefilter('ignore')
import os
from scipy.stats import rankdata
import talib as ta
##################一元函数########################
def log(x):
    return np.log(abs(x))

def abs(x):
    return np.abs(x)
    
def sqrt(x):
    return np.sqrt(x)

def rank(x):
    return x.rank(axis=1)

def inv(x):
    return 1.0/x
    
def percent(x):
    return x.div(x.sum(axis=1),axis=0)

def diff(df, window=1):

    return df.diff(window)
##################一元函数########################

##################二元函数########################
def delay(x,window):
    return x.shift(window)

def ts_mean(x,window):
    return x.rolling(window).mean()

def ts_std(x,window):
    return x.rolling(window).std()

def ts_sum(x,window):
    return x.rolling(window).sum()

# def ts_mul(x,window):
#     return x.rolling(window).max()

def ts_min(x,window):
    return x.rolling(window).min()

def ts_max(x,window):
    return x.rolling(window).max()

def ts_min_ind(x,window):
    return x.rolling(window).apply(lambda w :np.argmin(w))

def ts_max_ind(x,window):
    return x.rolling(window).apply(lambda w :np.argmax(w))

def ts_rank(x,window):
    return x.rolling(window).apply(lambda w :rankdata(w)[-1])

def ts_pct_change(x,window):
    return x.pct_change(window).sum()
##################二元函数########################

##################三元函数########################
def add(x,y):
    return np.add(x,y)
def sub(x,y):
    return np.subtract(x,y)   
def mul(x,y):
    return np.multiply(x,y) 
def div(x,y):
    return np.divide(x,y)
##################三元函数########################
##################元函数########################
def corr(x,y,window=5):
    return x.rolling(window).corr(y)
def cov(x,y,window=5):
    return x.rolling(window).cov(y)
##################4元函数########################
def vwap(h,l,v):
    return div((v*(h+l)/2).cumsum() , v.cumsum())
    
#################TA_Lib#############################
def EMA(x,window):
    return ta.EMA(x,window)
def MACD(x, fastperiod=12, slowperiod=26, signalperiod=9):
    return ta.MACD(x,fastperiod=12, slowperiod=26, signalperiod=9)








