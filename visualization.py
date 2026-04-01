import matplotlib.pyplot as plt
import numpy as np

def plot_kpis(months, revenue, costs, profit, revenue_growth, cost_growth):
    _, axs = plt.subplots(2, 1, figsize=(10, 14))

    # --- Line Charts ---
    axs[0].plot(months, revenue, marker='o', label="Revenue")
    axs[0].plot(months, costs, marker='o', label="Costs")
    axs[0].plot(months, profit, marker='o', label="Profit")
    axs[0].set_title("KPIs")
    axs[0].set_ylabel("USD")
    axs[0].grid()
    axs[0].legend()
                            
    # --- Bar Charts ---
    months_growth = months[1:]

    axs[1].bar(months_growth, revenue_growth, label="Revenue Growth")
    axs[1].bar(months_growth, cost_growth, alpha=0.6, label="Cost Growth")
    axs[1].set_title("Growth Rates")
    axs[1].set_ylabel("Growth (%)")
    axs[1].grid()
    axs[1].legend()

    plt.tight_layout()
    plt.show()
