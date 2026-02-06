import pandas as pd

import matplotlib
matplotlib.use("Agg") 
import matplotlib.pyplot as plt

FILE_NAME = "digital_behaviour.csv"
DAILY_LIMIT = 6.0
def load_data(filename):
    """
    Load data and convert Date column.
    """
    try:
        df = pd.read_csv(filename)
        df['Date'] = pd.to_datetime(df['Date'], format="%Y-%m-%d")
        df = df.sort_values(by="Date")
        
        return df
        
    except FileNotFoundError:
        print("Error: File not found.")
        return pd.DataFrame()
    

def visualize_digital_behavior(df):
    """
    Create a side-by-side plot layout.
    """

    # 1. Setup Subplots in 1 Row and 2 Columns
    fig, axes = plt.subplots(1, 2, figsize=(15, 5))

    # Assigning axes
    ax1 = axes[0]
    ax2 = axes[1]

    # Main title
    fig.suptitle("Project 3: Digital Behaviour Analysis")

    # === PLOT 1: Daily Trends (Line Plot) ===
    ax1.plot(df["Date"], df["ScreenTime"], label="Screen Time")

    ax1.plot(
        df["Date"],
        df["AppUsage"],
        linestyle="--",
        label="App Usage"
    )

    ax1.axhline(
        y=DAILY_LIMIT,
        color="red",
        linestyle="--",
        label="Daily Limit"
    )

    ax1.set_title("Daily Usage Trends")
    ax1.set_xlabel("Date")
    ax1.set_ylabel("Hours")
    ax1.legend()
    ax1.tick_params(axis="x", rotation=45)

    # === PLOT 2: Correlations (Scatter Plot) ===
    scatter = ax2.scatter(
        df["Unlocks"],
        df["ScreenTime"],
        c=df["AppUsage"],
        cmap="viridis",
        alpha=0.7
    )

    ax2.set_title("Unlocks vs. Screen Time")
    ax2.set_xlabel("Unlocks")
    ax2.set_ylabel("Screen Time")

    plt.colorbar(scatter, ax=ax2, label="App Usage (Hours)")

    # Save the figure
    plt.tight_layout()
    plt.savefig("digital_behaviour_analysis.png")

    print("Plot saved as 'digital_behaviour_analysis.png'")


if __name__ == "__main__":
    df = load_data(FILE_NAME)
    
    if not df.empty:
        visualize_digital_behavior(df)
