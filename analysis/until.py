import numpy as np
import pandas as pd
# import warnings; warnings.simplefilter('ignore')
import os
import matplotlib.pyplot as plt


def backtest_1(test_factor,megedata,Benchmark,tradeable,group_num=10,commision_fee=0):
    #不算复利
    test_factor=test_factor.replace([np.inf, -np.inf], np.nan)
    clean_factor_data=megedata
    input_factor= test_factor*tradeable
    input_factor=input_factor.stack()

    clean_factor_data["factor"]=input_factor
    clean_factor_data=clean_factor_data.dropna()
    clean_factor_data["factor_quantile"]=clean_factor_data["factor"].groupby(level=0).apply(lambda x :((pd.qcut(x, 10, labels=False,duplicates='drop') + 1)))

    long_portfolio_data = clean_factor_data[clean_factor_data['factor_quantile'] == group_num]
    short_portfolio_data = clean_factor_data[clean_factor_data['factor_quantile'] == 1]

    long_portfolio_rate_of_return = long_portfolio_data['period'].mean(level=0) - commision_fee
    short_portfolio_rate_of_return = short_portfolio_data['period'].mean(level=0) - commision_fee
    hedged_rate_of_return = long_portfolio_rate_of_return - short_portfolio_rate_of_return - 2 * commision_fee
    hedged_with_Benchmark_return = long_portfolio_rate_of_return - Benchmark - commision_fee

    long_cumulative_return = 1+long_portfolio_rate_of_return.cumsum()
    short_cumulative_return = 1+short_portfolio_rate_of_return.cumsum()
    hedged_cumulative_return = 1+hedged_rate_of_return.cumsum()
    Benchmark_cumulative_return = 1+Benchmark.cumsum()
    hedged_with_Benchmark_cumulative_return = 1+hedged_with_Benchmark_return.cumsum()

    Return = pd.concat([long_cumulative_return,short_cumulative_return, hedged_cumulative_return, Benchmark_cumulative_return,hedged_with_Benchmark_cumulative_return], axis=1)
    Return.columns = ['long','short','long-short','benchmark','long-benchmark']

    Return=Return.dropna()
    Return.plot(figsize=(16,9),title="test—factor")

