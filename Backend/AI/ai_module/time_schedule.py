import numpy as np
from datetime import datetime, timedelta

def generate_time_intervals(series):
    return [(series[i+1]-series[i]).total_seconds() for i in range(len(series)-1)]

# Определение коэффициентов автокорреляции
def autocorrelation(series, lag):
    y1 = series[:len(series) - lag]
    y2 = series[lag:]
    return np.corrcoef(y1, y2)[0, 1]

# Предсказание следующего значения ряда на основе значимых лагов
def predict_next_value(series, max_lag=0, p=0):
    datetime_intervals = generate_time_intervals(series)
    # Вычисление автокорреляций для лагов
    if max_lag == 0:
        max_lag = len(datetime_intervals) - 1
    lags = range(1, max_lag)
    autocorrelations = np.nan_to_num([autocorrelation(datetime_intervals, lag) for lag in lags])
    # Выбор самого значимого лага
    significant_lag = sorted(zip(lags, autocorrelations), key=lambda x: x[1], reverse=True)[0]
    print(significant_lag)
    return series[-1] + timedelta(seconds=series[-1] if significant_lag[1] < p else datetime_intervals[-significant_lag[0]])

# date_format = "%Y-%m-%d %H:%M:%S.%f"
# datetime_series = [
#     datetime.strptime("2024-10-11 19:41:03.709297", date_format),
#     datetime.strptime("2024-10-13 20:01:02.709297", date_format),  
#     datetime.strptime("2024-10-16 23:41:03.101", date_format),
#     datetime.strptime("2024-10-20 20:11:17.709297", date_format),
#     datetime.strptime("2024-10-22 19:55:56.709297", date_format),  
#     datetime.strptime("2024-10-25 19:41:03.709297", date_format),
# ]

# print(predict_next_value(datetime_series))
