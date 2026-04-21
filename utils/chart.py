import matplotlib.pyplot as plt
import os

STATIC_FOLDER = "static"

def plot_chart(counter):
    os.makedirs(STATIC_FOLDER, exist_ok=True)

    top = dict(counter.most_common(5))

    ips = list(top.keys())
    counts = list(top.values())

    plt.figure()
    plt.bar(ips, counts)
    plt.title("Top 5 IP Requests")
    plt.xticks(rotation=30)
    plt.tight_layout()

    path = os.path.join(STATIC_FOLDER, "chart.png")
    plt.savefig(path)
    plt.close()

    return "static/chart.png"