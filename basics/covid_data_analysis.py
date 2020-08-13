import xlwt
import pandas as pd

# Collect data from wikipedia
wiki = 'https://en.wikipedia.org/wiki/COVID-19_pandemic_in_India'
df = pd.read_html(wiki, match='State/Union Territory')[0]
print("Downloaded state wise data successfully!")

# Fix bad header
df.columns = [
    'State',
    'Total Cases',
    'Total Deaths',
    'Total Recoveries',
    'Col 5',
    'Col 6',
    'Col 7',
    'Col 8',
    'Col 9'
]

# Remove extra rows and Columns
df.drop([36, 37], axis=0, inplace=True)  # drop rows
df.drop(['Col 5', 'Col 6', 'Col 7', 'Col 8', 'Col 9'], axis=1, inplace=True)  # drop Columns

# Fix a value using regular expression
# Change the datatype of entire Column
df['Total Cases'] = df['Total Cases'].str.replace('\[.*\]|,', '', regex=True).apply(int)
df['Total Deaths'] = df['Total Deaths'].str.replace('\[.*\]|,', '', regex=True).apply(int)
df['Total Recoveries'] = df['Total Recoveries'].str.replace('\[.*\]|,', '', regex=True).apply(int)

# Sort data of a data frame in descending order
df.sort_values(by='Total Cases', ascending=False, inplace=True)

# Store data in csv or excel or html format
df.to_csv('covid_india.csv')
