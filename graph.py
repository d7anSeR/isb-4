import matplotlib.pyplot as plt


def create_stats(statistic: dict) -> plt.figure:
    fig = plt.figure(figsize=(30, 5))
    plt.ylabel("Time")
    plt.xlabel("Number of processes")
    plt.title("Dependence of execution time on the number of processes")
    x = statistic.keys()
    y = statistic.values()
    plt.bar(x, y, color="blue", width=0.05)
    plt.show(block = False)
    return fig