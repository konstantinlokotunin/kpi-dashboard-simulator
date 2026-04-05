from src.data_loader import load_data
from src.data_pandas import load_data_pandas
from src.analysis import calculate_profit, calculate_growth_rate, calculate_average, find_best_month, find_worst_month, export_results
from src.visualization import plot_kpis

def main():

    months, revenue, costs = load_data("data/data.csv")

    df = load_data_pandas("data/data.csv")

    profit = calculate_profit(revenue, costs)

    best_month, best_value = find_best_month(profit, months)
    worst_month, worst_value = find_worst_month(profit, months)

    average_revenue = round(calculate_average(revenue), 2)

    revenue_growth = calculate_growth_rate(revenue) * 100
    cost_growth = calculate_growth_rate(costs) * 100

    revenue_growth_lst = list(calculate_growth_rate(revenue))
    cost_growth_lst = list(calculate_growth_rate(costs))
    
    revenue_growth_str = ", ".join(f"{x: .2f}%" for x in revenue_growth_lst)
    cost_growth_str = ", ".join(f"{x: .2f}%" for x in cost_growth_lst)

    print(f"Best Month: {best_month} with {best_value} USD in profit.")
    print(f"Worst Month: {worst_month} with {worst_value} USD in profit.")
    print(f"Average Revenue: {average_revenue} USD")
    print("Revenue Growth Rates:", revenue_growth_str)
    print("Cost Growth Rates:", cost_growth_str)

    export_results("output.csv", months, revenue, costs, profit)
    print("Data exported to output.csv")

    plot_kpis(months, revenue, costs, profit, revenue_growth, cost_growth)

    print(df.head())

if __name__ == "__main__":
    main()