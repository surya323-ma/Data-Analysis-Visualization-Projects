import pandas as pd
def load_data(filename):
    """
    Load Virat Kohli match-wise performance data and parse dates.
    """
    try:
        df = pd.read_csv(filename)
        df["match_date"] = pd.to_datetime(df["match_date"], format="%Y-%m-%d")
        
        return df
    except FileNotFoundError:
        print(f"Error: {filename} not found.")
        return pd.DataFrame()
    except Exception:
        print(f"Error loading data.")
        return pd.DataFrame()

def load_opponent_data(filename):
    try:
        df = pd.read_csv(filename)
        return df
    except FileNotFoundError:
        print(f"Error: {filename} not found.")
        return pd.DataFrame()
def merge_match_opponent(match_df, opponent_df):
    """
    Merge match data with opponent full names.
    """

    if "opponent" not in match_df.columns or "opponent" not in opponent_df.columns:
        print("Error: 'opponent' column missing in one of the datasets.")
        return match_df
    merged_df = pd.merge(
        match_df,
        opponent_df,
        on="opponent",
        how="left"
    )
    
    return merged_df
def total_runs(df):
    """
    Calculate total runs scored by Virat Kohli.
    """
    runs_column = df["runs"]
    total = runs_column.sum()
    return total
def average_runs(df):
    """
    Calculate the average runs per match scored by Virat Kohli.
    """
    runs_column = df["runs"]    
    average = runs_column.mean()
    average_rounded = round(average, 2)    
    return average_rounded
def runs_by_opponent(df):
    """
    Calculate total runs scored against each opponent.
    """
    grouped_data = df.groupby("fullName")
    total_runs = grouped_data["runs"].sum()
    sorted_runs = total_runs.sort_values(ascending=False)
    return sorted_runs
def count_fifties(df):
    """
    Count the number of matches where Virat Kohli scored fifty or more runs (but less than 100 runs).
    """
    total_fifties = df[(df["runs"] >= 50) & (df["runs"] < 100)].shape[0]

    return total_fifties


def count_centuries(df):
    """
    Count the number of matches where Virat Kohli scored a century or more runs.
    """
    total_centuries = df[df["runs"] >= 100].shape[0]

    return total_centuries


def career_run_progression(df):
    """
    Calculate cumulative career runs over time.
    """
    # Sort by match date
    df_sorted = df.sort_values("match_date")

    # Cumulative sum of runs
    cumulative_runs = df_sorted["runs"].cumsum()

    # Create career_runs column
    df_sorted["career_runs"] = cumulative_runs

    # Select required columns
    result = df_sorted[["match_date", "runs", "career_runs"]]

    return result


def consistency_matches(df):
    """
    Count the number of matches where Virat Kohli scored at least 30 runs.
    """
    total_consistent_matches = df[df["runs"] >= 30].shape[0]

    return total_consistent_matches
def not_out_innings(df):
    """
    Count the number of innings where Virat Kohli remained Not Out.
    """
    total_not_out = df[df["dismissal"] == "Not Out"].shape[0]

    return total_not_out
def best_venue(df):
    """
    Find the venue where Virat Kohli has scored the most runs.
    """
    best_venue = (
        df.groupby("venue")["runs"]
        .sum()
        .sort_values(ascending=False)
        .head(1)
    )
    return best_venue
if __name__ == "__main__":
    print("### Virat Kohli Career Analysis ###")
    virat_df = load_data("ipl_matches.csv")
    opponent_df = load_opponent_data("opponents.csv")

    if not virat_df.empty:
        if not opponent_df.empty:
            df = merge_match_opponent(virat_df, opponent_df)
        else:
            df = virat_df
            print("Warning: Opponent data missing, proceeding with match data only.")
        print(f"\nTotal Career Runs: {total_runs(df)}")
        print(f"Average Runs Per Match: {average_runs(df)}")
        print("\nRuns Against Each Opponent (Top 3):")
        print(runs_by_opponent(df).head(3))
        print(f"\nNumber of 50s: {count_fifties(df)}")
        print(f"Number of Centuries: {count_centuries(df)}")
        print("\nCareer Run Progression (First 5 matches):")
        print(career_run_progression(df).head())
        print(f"\nNumber of Consistent Matches (30+ runs):")
        print(f"{consistency_matches(df)}")
        print(f"Number of Not Out Innings:")
        print(f"{not_out_innings(df)}")
        best = best_venue(df)
        print(f"\nBest Venue: {best.index[0]} with {best.values[0]} runs")
