import matplotlib.pyplot as plt


def create_graph(statistic: dict, path_file: str) -> plt.figure:
    """the function creates a time schedule for different pools"""
    fig = plt.figure(figsize=(18, 9))
    x = statistic.keys()
    y = statistic.values()
    plt.xlabel('Processes')
    plt.ylabel('Time')
    plt.title('Statistics')
    plt.bar(x, y, color='blue', width=0.5)
    plt.savefig(path_file)
