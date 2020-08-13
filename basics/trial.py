import pandas as pd

# drinks = pd.read_csv('http://bit.ly/drinksbycountry')
drinks = pd.read_csv('drinks.csv')
drinks.set_index('country', inplace=True)

print(drinks.head())
print(drinks.continent.head())

print(drinks.continent.value_counts())
print('Asia:', drinks.continent.value_counts()['Asia'])

# Sort by index names
print(drinks.continent.value_counts().sort_index())

# Sort by values present
print(drinks.continent.value_counts().sort_values())

# Create beer servings for Albania and Andorra
population = pd.Series(
    [2000000, 3000000],
    name='population',
    index=['Albania', 'Andorra']
)
# print()
# print(population)

# Add population to the drinks data frame
drinks = pd.concat([drinks, population], axis=1)
print()
print(drinks.head())

# Add total beer servings per population (Alignment)
total_beer_servings = drinks.beer_servings * population
print()
print(total_beer_servings)

