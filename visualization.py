import matplotlib.pyplot as plt
import numpy as np
import mplcursors

cursor = mplcursors.cursor(hover=True)

@cursor.connect("add")
def on_add(sel):
    sel.annotation.set_text(
    f"Month: {months[int(sel.target[0])]}\nProfit: {sel.target[1]:.1f}"
)

plt.style.use("seaborn-v0_8")

def plot_kpis(months, revenue, costs, profit, revenue_growth, cost_growth):
    _, axs = plt.subplots(2, 1, figsize=(2.5, 8))

    # --- Line Charts ---
    colors_plot = ["#4C72B0", "#912F56", "#040926"]
    
    axs[0].plot(months, revenue, marker='o', linewidth=2, label="Revenue", color=colors_plot[0])
    axs[0].plot(months, costs, marker='o', linewidth=2, label="Costs", color=colors_plot[1])
    axs[0].plot(months, profit, marker='o', linewidth=2, label="Profit", color=colors_plot[2])
    axs[0].set_title("KPI Trends", fontsize=14, fontweight="bold")
    axs[0].set_ylabel("USD")
    axs[0].grid(True, linestyle='--', alpha=0.6)
    axs[0].legend()

    # Highlight max profit point
    max_idx = profit.argmax()
    axs[0].scatter(months[max_idx], profit[max_idx], s=120, color=colors_plot[2])
    axs[0].annotate(
        "Peak Profit",
        (months[max_idx], profit[max_idx]),
        fontsize=9, fontweight="bold",
        color="black",
        textcoords="offset points",
        xytext=(0, 10),
        ha='center'
)
                            
    # --- Bar Charts ---
    months_growth = months[1:]
    x = np.arange(len(months_growth))

    colors_bar = ["#4C72B0", "#912F56"]

    width = 0.25

    axs[1].bar(x - width/2, revenue_growth, width, label="Revenue Growth", color=colors_bar[0])
    axs[1].bar(x + width/2, cost_growth, width, label="Cost Growth", color=colors_bar[1])

    for i, v in enumerate(revenue_growth):
        axs[1].text(i - width/2, v, f"{v:.1f}%", ha='center', va='bottom')

    for i, v in enumerate(cost_growth):
        axs[1].text(i + width/2, v, f"{v:.1f}%", ha='center', va='bottom')

    axs[1].set_xticks(x)
    axs[1].set_xticklabels(months_growth)

    axs[1].set_title("Monthly Growth Rates (%)", fontsize=14, fontweight="bold")
    axs[1].set_ylabel("Growth (%)")

    axs[1].set_ylim(min(min(revenue_growth), min(cost_growth)) - 5,
                max(max(revenue_growth), max(cost_growth)) + 5)

    axs[1].axhline(0, color='black', linewidth=1)
    axs[1].grid(axis='y', linestyle='--', alpha=0.6)
    axs[1].legend()
    
    plt.tight_layout()
    plt.show()


