import numpy as np

def calculate_profit(revenue, costs):
    revenue_arr = np.array(revenue)
    costs_arr = np.array(costs)
    
    return revenue_arr - costs_arr

def calculate_growth_rate(values):
    values_arr = np.array(values)
    
    growth_rates = (values_arr[1:] - values_arr[:-1]) / values_arr[:-1]
    
    return growth_rates

def calculate_average(values):
    return np.mean(values)

def find_max(values):
    return np.max(values)

def find_min(values):
    return np.min(values)
