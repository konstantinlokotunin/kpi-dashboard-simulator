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

def find_best_month(values, months):
    idx = np.argmax(values)
    return months[idx], values[idx]

def find_worst_month(values, months):
    idx = np.argmin(values)
    return months[idx], values[idx]

def export_results(filename, months, revenue, costs, profit):

    with open(filename, "w", newline="") as file:
        writer = csv.writer(file, delimiter=";")
        writer.writerow(["Month", "Revenue", "Costs", "Profit"])

        for i in range(len(months)):
            writer.writerow([months[i], revenue[i], costs[i], profit[i]])
