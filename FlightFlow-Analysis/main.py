import pandas as pd
FILE_NAME = "flights.csv"

# 1. Data Loading and Data Parsing
def load_flight_data(filename):
    """
    Load flight dataset and parse dates from 'FlightDate'.
    """
    try:
        # Load the CSV file into a Pandas DataFrame
        df = pd.read_csv(filename)
        if "FlightDate" not in df.columns:
            print("Error: 'FlightDate' column is missing in the CSV.")
            return pd.DataFrame()
        df["FlightDate"] = pd.to_datetime(df["FlightDate"], format="%Y-%m-%d")
        return df
        
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return pd.DataFrame()
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return pd.DataFrame()


# 2. Data Cleaning
def clean_delay_data(df):
    """
    Assumption: If delay is NaN (empty), it means the flight was On Time (0 delay).
    """
    if "DepartureDelay" in df.columns:
        df["DepartureDelay"] = df["DepartureDelay"].fillna(0)
    
    return df
# 3. Feature Extraction
def extract_day_features(df):
    """
    Extract the 'Day Name' (Monday, Tuesday...) from the Date column.
    """
    df["Day_Name"] = df["FlightDate"].dt.day_name()
    return df
# 4. Statistical Analysis
def airline_reliability_stats(df):
    """
    Calculate the Average Departure Delay and Total Flights for each airline.
    """
    stats = (
        df.groupby("Airline")["DepartureDelay"]
        .agg(["mean", "count"])
    )
    if not stats.empty:
        stats = stats.rename(columns={"mean": "Avg_Delay", "count": "Total_Flights"})
        stats["Avg_Delay"] = stats["Avg_Delay"].round(2)
    return stats
# 5. Ranking & Sorting
def rank_airlines(stats_df):
    """
    Rank airlines from Most Reliable (Lowest Delay) to Least Reliable.
    """
    sorted_stats = stats_df.sort_values(by="Avg_Delay", ascending=True)
    return sorted_stats
# 6. Pattern Identification
def identify_delayed_days(df):
    """
    Find which day of the week has the worst delays on average.
    """
    day_stats = df.groupby("Day_Name")["DepartureDelay"].mean()
    
    # Sort days by highest delay first and round values
    sorted_days = day_stats.sort_values(ascending=False).round(2)
    
    return sorted_days


if __name__ == "__main__":
    print("### FlightFlow Analysis ###")
    raw_df = load_flight_data(FILE_NAME)
    if not raw_df.empty:
        clean_df = clean_delay_data(raw_df)
        print(f"Data Loaded & Cleaned: {clean_df.shape[0]} flights processed.")
        enhanced_df = extract_day_features(clean_df)
        stats = airline_reliability_stats(enhanced_df)
        ranked = rank_airlines(stats)
        print("\nMost Reliable Airlines (Lowest Avg Delay):")
        print(ranked.head(3))
        print("\nLeast Reliable Airlines (Highest Avg Delay):")
        print(ranked.tail(3))
        worst_days = identify_delayed_days(enhanced_df)
        print("\nWorst Days to Fly (Highest Avg Delay):")
        print(worst_days.head(3))
    else:
        print("Analysis could not proceed due to data loading errors.")
