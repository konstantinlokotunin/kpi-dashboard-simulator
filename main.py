from data import kpi_data
from analysis import calculate_profit, calculate_growth_rate, calculate_average, find_max, find_min
from visualization import plot_kpis

def main():
    months = kpi_data["months"]
    revenue = kpi_data["revenue"]
    costs = kpi_data["costs"]

    profit = calculate_profit(revenue, costs)

    revenue_growth = calculate_growth_rate(revenue)
    cost_growth = calculate_growth_rate(costs)

    print("Average Revenue:", calculate_average(revenue))
    print("Revenue Growth Rates:", revenue_growth)
    print("Max Revenue:", find_max(revenue))
    print("Min Revenue:", find_min(revenue))
    print("Cost Growth Rates:", cost_growth)

    plot_kpis(months, revenue, costs, profit)

if __name__ == "__main__":
    main()
