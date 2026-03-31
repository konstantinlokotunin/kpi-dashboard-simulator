import matplotlib.pyplot as plt

def plot_kpis(months, revenue, costs, profit):
    fig, axs = plt.subplots(3, 1, figsize=(8, 10), sharex=True)

    axs[0].plot(months, revenue)
    axs[0].set_title("Revenue")

    axs[1].plot(months, costs)
    axs[1].set_title("Costs")

    axs[2].plot(months, profit)
    axs[2].set_title("Profit")

    for ax in axs:
        ax.set_xlabel("Month")
        ax.set_ylabel("USD")

    fig.suptitle("Company KPI Overview")

    plt.tight_layout()
    plt.show()
