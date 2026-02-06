import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import matplotlib
matplotlib.use("Agg")  # Headless mode for saving files

# Constants
FILE_NAME = "instagram_dataset.csv"

# Set a clean visual theme
sns.set_theme(style="whitegrid")


# 1. === Loading Instagram Data ===
def load_instagram_data(filename):
    """
    Loading Instagram post dataset.
    """
    try:
        # Read the CSV file into a dataframe
        df = pd.read_csv(filename)
        
        print(f"Data Loaded Successfully: {len(df)} posts.")
        print(f"Columns: {list(df.columns)}")
        
        # Return the dataframe
        return df

    except FileNotFoundError:
        print(f"Error: {filename} not found.")
        return pd.DataFrame()



# 2. === Correlation Heatmap ===
def plot_engagement_correlation(df):
    """
    Visualize correlation between engagement metrics using a Heatmap.
    """
    # Numeric engagement columns
    engagement_cols = [
        "likes",
        "comments",
        "shares",
        "saves",
        "reach"
    ]
    
    # Calculate correlation matrix
    corr_matrix = df[engagement_cols].corr()

    # Set figure size
    plt.figure(figsize=(10, 8))

    # Create Heatmap
    sns.heatmap(
        corr_matrix,
        annot=True,
        cmap="coolwarm",
        fmt=".2f",
        linewidths=0.5
    )

    # Title
    plt.title("Instagram Engagement Correlation Heatmap")
    
    # Adjust layout
    plt.tight_layout()
    
    # Save plot
    plt.savefig("engagement_correlation_heatmap.png")
    
    print("Saved: engagement_correlation_heatmap.png")



# 3. === Hashtag Impact Trend (Regression Plot) ===
def plot_hashtag_vs_reach(df):
    """
    Analyze relationship between hashtags and reach using Regression.
    """
    # Set figure size
    plt.figure(figsize=(10, 6))

    # Regression Plot
    sns.regplot(
        x="hashtags_count",
        y="reach",
        data=df,
        scatter_kws={"color": "green"},
        line_kws={"color": "red"}
    )

    # Titles and labels
    plt.title("Hashtag Count vs. Reach Trend")
    plt.xlabel("Number of Hashtags")
    plt.ylabel("Post Reach")

    # Adjust layout and save
    plt.tight_layout()
    plt.savefig("hashtag_reach_trend.png")
    
    print("Saved: hashtag_reach_trend.png")



# 4. === Residual Analysis (Unexpected Viral Behavior) ===
def plot_residual_analysis(df):
    """
    Use a Residual Plot to see 'outlier' performance.
    Points far from 0 line = Posts performing much better/worse than expected.
    """
    # Set figure size
    plt.figure(figsize=(10, 6))

    # Residual Plot
    sns.residplot(
        x="hashtags_count",
        y="reach",
        data=df,
        color="purple"
    )

    # Reference line at y=0
    plt.axhline(0, color="black", linestyle="--")

    # Titles and labels
    plt.title("Residual Analysis: Viral Outliers (Observed - Expected)")
    plt.xlabel("Number of Hashtags")
    plt.ylabel("Residual Reach (Deviation)")

    # Adjust layout and save
    plt.tight_layout()
    plt.savefig("viral_residual_analysis.png")
    
    print("Saved: viral_residual_analysis.png")



if __name__ == "__main__":
    print("### Instagram Viral Trends Analytics ###")

    df = load_instagram_data(FILE_NAME)

    if not df.empty:
        # 1. Correlation Analysis (Heatmap)
        plot_engagement_correlation(df)

        # 2. Hashtag Trend Analysis (Regression)
        plot_hashtag_vs_reach(df)

        # 3. Residual Analysis (Residplot)
        plot_residual_analysis(df)

    else:
        print("Analysis stopped.")
