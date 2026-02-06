# FlightFlow Analysis Project
Air travel plays a major role in today’s fast-moving world, but delays can turn even a short journey into a frustrating experience.
Chef is planning multiple domestic and international trips. To avoid unnecessary delays, he has collected real-world flight data containing information such as:

Flight dates
Airlines
Departure delays
Chef needs your help to analyze this dataset. Your task is to use the Pandas library to clean, analyze, and extract meaningful insights from flight delay data.

What’s Already Provided
You are given a single file: main.py

All required function names are already defined.
The program flow is already set up.
You only need to complete the missing logic using the Pandas Library.
Do NOT change function names or print statements.
Dataset
In this Project, you will work with a CSV file named: flights.csv

This dataset contains flight departure information.
Columns:
FlightDate → Date of the flight (YYYY-MM-DD)
Airline → Name of the airline
Origin → Departure airport or city code
Destination → Arrival airport or city code
DepartureDelay → Delay in minutes
If missing (NaN), it means the flight was on time.
Cancelled → Indicates whether the flight was cancelled.
0 = Not cancelled
1 = Cancelled
Dataset Preview (First 5 rows):
FlightDate,Airline,Origin,Destination,DepartureDelay,Cancelled
2024-04-02,Akasa Air,DOH,SIN,103,1
2024-01-04,Singapore Airlines,JFK,DOH,20,0
2024-05-24,Akasa Air,SIN,LHR,57,1  
2024-02-03,IndiGo,LHR,MUM,31,1
2024-04-07,Singapore Airlines,LHR,BLR,15,0
Your Tasks
Load Flight Data
Inside load_flight_data(filename):
Load the CSV file using Pandas.
Convert the FlightDate column into datetime format.
Use the format: "YYYY-MM-DD".
Docs: pandas.read_csv() | pandas.to_datetime()
Clean Delay Data
Inside clean_delay_data(df):
If DepartureDelay is missing (NaN), treat it as 0 minutes.
This means the flight departed on time.
Goal: Fill missing values (NaN) in the DepartureDelay column with 0.
Docs: fillna()
Extract Day Features
Inside extract_day_features(df):
Extract the day name from the flight date. Example:
2024-01-01 → Monday
2024-01-02 → Tuesday
Store it in a new column called Day_Name.
Docs: pandas.Series.dt.day_name()
Airline Reliability Analysis
Inside airline_reliability_stats(df):
For each airline, calculate:
Avg_Delay → The mean of the departure delay.
Total_Flights → The count of how many flights they operated.
Requirements:
Group by Airline.
Round average delay to 2 decimal places.
Docs: groupby() | agg() | round()
Rank Airlines by Reliability
Inside rank_airlines(stats_df):
Rank airlines from:
Most reliable (lowest average delay)
Least reliable (highest average delay)
Goal: Sort your reliability stats so that the Most Reliable airline (Lowest Average Delay) appears at the top.
Docs: sort_values()
Identify Worst Days to Fly
Inside identify_delayed_days(df):
Calculate average delay for each day of the week.
Sort days from highest delay to lowest.
Round values to 2 decimal places.
Docs: groupby() | mean() | sort_values()
