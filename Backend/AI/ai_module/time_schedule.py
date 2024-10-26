import numpy as np
from datetime import datetime, timedelta

def generate_time_intervals(series):
    return [(series[i+1]-series[i]).seconds for i in range(len(series)-1)]

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
    return series[-1] + (series[-1] if significant_lag[1] < p else datetime_intervals[-significant_lag[0]])


# datetime_series = [1, 3, 6, 11, 13, 16]
# # datetime_series = [1, 2, 3, 4, 5, 6]
# predicted_value = predict_next_value(datetime_series)

# # Вывод результатов
# print("Предсказанное значение следующего элемента ряда:", predicted_value)