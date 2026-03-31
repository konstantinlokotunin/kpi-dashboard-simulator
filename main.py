from data import kpi_data
from analysis import calculate_profit, calculate_average, find_max, find_min
from visualization import plot_kpis

def main():
    months = kpi_data["months"]
    revenue = kpi_data["revenue"]
    costs = kpi_data["costs"]

    profit = calculate_profit(revenue, costs)

    print("Average Revenue:", calculate_average(revenue))
    print("Max Revenue:", find_max(revenue))
    print("Min Revenue:", find_min(revenue))

    plot_kpis(months, revenue, costs, profit)


if __name__ == "__main__":
    main()
