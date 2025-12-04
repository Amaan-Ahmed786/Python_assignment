# codefiles/visualize.py
import matplotlib.pyplot as plt
import pandas as pd

def create_dashboard(daily_df, weekly_df, df, outpath="output/dashboard.png"):

    fig, ax = plt.subplots(3, 1, figsize=(12, 15), constrained_layout=True)

    # Daily Trend Line
    for b in daily_df["building"].unique():
        temp = daily_df[daily_df["building"] == b]
        ax[0].plot(temp["timestamp"], temp["kwh"], label=b)
    ax[0].set_title("Daily Energy Consumption")
    ax[0].legend()

    # Weekly Bar Graph
    avg_week = weekly_df.groupby("building")["kwh"].mean()
    ax[1].bar(avg_week.index, avg_week.values)
    ax[1].set_title("Average Weekly Usage")

    # Peak Hour Scatter Plot
    df["timestamp"] = pd.to_datetime(df["timestamp"])
    hourly = df.groupby(["timestamp", "building"])["kwh"].sum().reset_index()
    top = hourly.sort_values("kwh", ascending=False).groupby("building").head(10)

    for b in top["building"].unique():
        t = top[top["building"] == b]
        ax[2].scatter(t["timestamp"], t["kwh"], label=b)

    ax[2].set_title("Top Peak Consumption Hours")
    ax[2].legend()

    plt.savefig(outpath, dpi=150)
    plt.close()
