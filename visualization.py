import matplotlib.pyplot as plt
import numpy as np

def plot_kpis(months, revenue, costs, profit, revenue_growth, cost_growth):
    _, axs = plt.subplots(2, 1, figsize=(2.5, 8))

    # --- Line Charts ---
    axs[0].plot(months, revenue, marker='o', label="Revenue")
    axs[0].plot(months, costs, marker='o', label="Costs")
    axs[0].plot(months, profit, marker='o', label="Profit")
    axs[0].set_title("KPIs")
    axs[0].set_ylabel("USD")
    axs[0].grid(axis='x', linestyle='--', alpha=0.7)
    axs[0].legend()
                            
    # --- Bar Charts ---
    months_growth = months[1:]
    x = np.arange(len(months_growth))

    width = 0.35

    axs[1].bar(x - width/2, revenue_growth, width, label="Revenue Growth")
    axs[1].bar(x + width/2, cost_growth, width, label="Cost Growth")

    for i, v in enumerate(revenue_growth):
        axs[1].text(i - width/2, v, f"{v:.1f}%", ha='center', va='bottom')

    for i, v in enumerate(cost_growth):
        axs[1].text(i + width/2, v, f"{v:.1f}%", ha='center', va='bottom')

    axs[1].set_xticks(x)
    axs[1].set_xticklabels(months_growth)

    axs[1].set_title("Growth Rates (%)")
    axs[1].set_ylabel("Growth (%)")

    axs[1].set_ylim(min(min(revenue_growth), min(cost_growth)) - 5,
                max(max(revenue_growth), max(cost_growth)) + 5)

    axs[1].grid(axis='y', linestyle='--', alpha=0.7)
    axs[1].legend()
    
    plt.tight_layout()
    plt.show()

