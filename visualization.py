import matplotlib.pyplot as plt

def plot_kpis(months, revenue, costs, profit):
    fig, axs = plt.subplots(3, 1, figsize=(8, 10))

    # Revenue
    axs[0].plot(months, revenue)
    axs[0].set_title("Revenue")
    axs[0].set_ylabel("USD")

    # Costs
    axs[1].plot(months, costs)
    axs[1].set_title("Costs")
    axs[1].set_ylabel("USD")

    # Profit
    axs[2].plot(months, profit)
    axs[2].set_title("Profit")
    axs[2].set_ylabel("USD")
    axs[2].set_xlabel("Month")

    plt.tight_layout()
    plt.show()
