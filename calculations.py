import numpy as np
import pandas as pd


def calculations_daily_volatility(data: pd.DataFrame):
    data['Daily Returns '] = data['Close '].pct_change()
    Daily_Volatility = np.std(data['Daily Returns '].dropna())
    return Daily_Volatility


def calculations_annualized_volatility(daily_volatility: float, data: pd.DataFrame):
    length_of_data = len(data)
    Annualized_Volatility = daily_volatility * length_of_data
    return Annualized_Volatility
