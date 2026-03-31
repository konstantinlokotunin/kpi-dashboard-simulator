def calculate_profit(revenue, costs):
    profit = []
    
    for i in range(len(revenue)):
        profit.append(revenue[i] - costs[i])
    
    return profit


def calculate_average(values):
    return sum(values) / len(values)


def find_max(values):
    return max(values)


def find_min(values):
    return min(values)
