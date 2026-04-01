import matplotlib.pyplot as plt
import numpy as np

def plot_kpis(months, revenue, costs, profit, revenue_growth, cost_growth):
    fig, axs = plt.subplots(4, 1, figsize=(10, 14)

    # --- Line Charts ---
    axs[0].plot(months, revenue, marker='o', label="Revenue")
    axs[0].set_title("Revenue")
    axs[0].grid()
    axs[0].legend()

    axs[1].plot(months, costs, marker='o', label="Costs")
    axs[1].set_title("Costs")
    axs[1].grid()
    axs[1].legend()

    axs[2].plot(months, profit, marker='o', label="Profit")
    axs[2].set_title("Profit")
    axs[2].grid()
    axs[2].legend()
                            
    # --- Bar Charts ---
    months_growth = months[1:]

    axs[3].bar(months_growth, revenue_growth, label="Revenue Growth")
    axs[3].bar(months_growth, cost_growth, alpha=0.6, label="Cost Growth")

    axs[3].set_title("Growth Rates")
    axs[3].set_ylabel("Growth")
    axs[3].grid()
    axs[3].legend()

    plt.tight_layout()
    plt.show()
