import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Read in merged_dataset.csv
df = pd.read_csv("your/path/ai-healthcare/merged_dataset.csv")
# Convert 'date' column to datetime
df['date'] = pd.to_datetime(df['date'], format='%Y%m%d')
# Record the date that separate pre and during Covid
date_split = pd.to_datetime("2020-03-11")

# Impute sleep data

# Initialize a copy
df_filtered = df.copy()

# Replace 0 with 0.1 in 'sleep_duration_hours' and 'sleep_heathkit_dur'
df['sleep_duration_hours'] = df['sleep_duration_hours'].replace(0, 0.1)
df['sleep_heathkit_dur'] = df['sleep_heathkit_dur'].replace(0, 0.1)

# Step 1: Calculate fold difference and absolute hour difference, ignoring NaNs
df['fold_difference'] = df.apply(
    lambda row: max(row['sleep_duration_hours'], row['sleep_heathkit_dur']) / min(row['sleep_duration_hours'], row['sleep_heathkit_dur']) 
    if pd.notna(row['sleep_duration_hours']) and pd.notna(row['sleep_heathkit_dur']) else None, axis=1
)

df['hour_difference'] = df.apply(
    lambda row: abs(row['sleep_duration_hours'] - row['sleep_heathkit_dur']) 
    if pd.notna(row['sleep_duration_hours']) and pd.notna(row['sleep_heathkit_dur']) else None, axis=1
)

# Step 2: Set values in both sleep columns to NaN if they don't pass the filter criteria
def filter_sleep_values(row):
    if pd.notna(row['fold_difference']) and row['fold_difference'] > 1.5 and \
       pd.notna(row['hour_difference']) and row['hour_difference'] > 2:
        return pd.Series([np.nan, np.nan])
    else:
        return pd.Series([row['sleep_duration_hours'], row['sleep_heathkit_dur']])

df_filtered[['sleep_duration_hours', 'sleep_heathkit_dur']] = df.apply(filter_sleep_values, axis=1)

df_filtered = df_filtered.iloc[:, :-2]

# Calculate daily mean and standard deviation across all students
filtered_daily_sleep = df_filtered.groupby(['date', 'id'])['sleep_duration_hours'].mean().reset_index()
filtered_sleep_stats = filtered_daily_sleep.groupby('date')['sleep_duration_hours'].agg(['mean', 'std']).reset_index()

# Identify dates that have a mean sleep hour being more than 9 more less than 6
# These dates likely contain error, as they appear as outliers during pre-processing
invalid_dates = filtered_sleep_stats[(filtered_sleep_stats['mean'] < 6) | (filtered_sleep_stats['mean'] > 9)]['date']

# Set sleep_duration_hours and sleep_heathkit_dur to NaN for rows with invalid dates
df_filtered.loc[df_filtered['date'].isin(invalid_dates), ['sleep_duration_hours', 'sleep_heathkit_dur']] = pd.NA

# Impute NA data

# Remove rows that contain no information
columns_to_check = list(range(2, 10)) + [12] + list(range(14, 16))

df_filtered = df_filtered[~(
    df_filtered.iloc[:, columns_to_check].isna().all(axis=1) &
    (df_filtered.iloc[:, 11].isna() | (df_filtered.iloc[:, 11] == 0))
)]

# Add information related to semesters

# A dictionary with the last days of classes for each semester
# This information is not yet used
last_days = {
    2017: ['2017-08-23', '2017-11-14'],
    2018: ['2018-03-06', '2018-05-30', '2018-08-22', '2018-11-13'],
    2019: ['2019-03-06', '2019-08-21', '2019-11-22'],
    2020: ['2020-03-06', '2020-06-03', '2020-08-26', '2020-11-17'],
    2021: ['2021-03-10', '2021-06-02', '2021-08-25', '2021-11-16'],
    2022: ['2022-03-08', '2022-06-01', '2022-08-24', '2022-11-15']
}

# Another dictionary listing the spring and fall semester dates
date_ranges = [
    ("2017-09-11", "2017-11-22"),
    ("2018-01-03", "2018-03-13"),
    ("2018-03-26", "2018-06-05"),
    ("2018-09-12", "2018-11-21"),
    ("2019-01-03", "2019-03-13"),
    ("2019-03-25", "2019-06-04"),
    ("2019-09-16", "2019-11-27"),
    ("2020-01-06", "2020-03-13"),
    ("2020-03-30", "2020-06-09"),
    ("2020-09-14", "2020-12-04"),
    ("2021-01-07", "2021-03-17"),
    ("2021-03-29", "2021-06-08"),
    ("2021-09-13", "2021-11-24"),
    ("2022-01-04", "2022-03-15"),
    ("2022-03-28", "2022-06-07"),
    ("2022-09-12", "2022-11-23")
]

date_ranges = [(pd.to_datetime(start), pd.to_datetime(end)) for start, end in date_ranges]

# Function to check if a date is within any of the specified date ranges
def is_break(date):
    return not any(start <= date <= end for start, end in date_ranges)

# Add the "is_break" column to the general DataFrame
df_filtered['is_break'] = df_filtered['date'].apply(is_break)

# Splitting the dataset

# Split the dataset into pre-COVID and during-COVID
pre_covid = df_filtered[df_filtered['date'] < date_split]
dur_covid = df_filtered[df_filtered['date'] >= date_split]

# Export and save the csv files
pre_covid.to_csv("your/path/pre_covid.csv", index=False)
dur_covid.to_csv("your/path/dur_covid.csv", index=False)