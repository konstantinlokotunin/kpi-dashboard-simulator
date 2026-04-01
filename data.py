# Monthly KPI data for a fictional company

import csv

def load_data(filepath):
    months = []
    revenue = []
    costs = []

    with open(filepath, newline="") as file:
        reader = csv.DictReader(file)
        
        for row in reader:
            months.append(row["month"])
            revenue.append(float(row["revenue"]))
            costs.append(float(row["costs"]))

    return months, revenue, costs
