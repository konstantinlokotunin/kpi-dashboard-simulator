from data import kpi_data
from analysis import calculate_profit, calculate_growth_rate, calculate_average, find_max, find_min
from visualization import plot_kpis

def main():
    months = kpi_data["months"]
    revenue = kpi_data["revenue"]
    costs = kpi_data["costs"]

    profit = calculate_profit(revenue, costs)

    best_month, best_value = find_best_month(profit, months)
    worst_month, worst_value = find_worst_month(profit, months)

    average_revenue = round(calculate_average(revenue), 2)

    revenue_growth_lst = list(calculate_growth_rate(revenue))
    cost_growth_lst = list(calculate_growth_rate(costs))
    
    revenue_growth = ", ".join(f"{x: .2%}" for x in revenue_growth_lst)
    cost_growth = ", ".join(f"{x: .2%}" for x in cost_growth_lst)

    print(f"Best Month: {best_month}, Profit: {best_value} USD")
    print(f"Worst Month: {worst_month}, Profit: {worst_value} USD")
    print(f"Average Revenue: {average_revenue} USD")
    print("Revenue Growth Rates:", revenue_growth)
    print("Cost Growth Rates:", cost_growth)

    plot_kpis(months, revenue, costs, profit, revenue_growth, cost_growth)

if __name__ == "__main__":
    main()
