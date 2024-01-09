import pandas as pd

# Read in compressed csv file
reviews = pd.read_csv('data/winemag-data-130k-v2.csv.zip', compression='zip')


# Group by 'country' servies and calculate the count and mean
grouped_df = reviews.groupby('country').agg(
    {'country': 'count', 'points': 'mean'})


# Rename columns for clarity
grouped_df.columns = ['count', 'points']

# Round 'points' to one decimal place
grouped_df['points'] = grouped_df['points'].round(1)

# Reset index to make 'country' a column
grouped_df = grouped_df.reset_index()


# Print out dataframe to csv file in data folder
grouped_df.to_csv('./data/reviews-per-country.csv', index=False)
