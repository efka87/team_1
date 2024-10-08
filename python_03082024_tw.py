# -*- coding: utf-8 -*-
"""python_03082024_tw.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Za8k_b_aZkiTKwH9_adCCCbTdov8bXml
"""

# required library import
import pandas as pd #analysis
import matplotlib.pyplot as plt # visualisation
pokemon_data = pd.read_csv('/content/Pokemon.csv')

# Pokemons % with type 1 == "water"
total_pokemon = len(pokemon_data)
water_pokemon = len(pokemon_data[pokemon_data['Type 1'] == 'Water'])
water_percentage = (water_pokemon / total_pokemon) * 100
print(f'Percentage of water pokemons: {water_percentage:.2f}%')

# What is the maximum 'Speed' value?
# What is the minimum 'Speed' value?
# What is the difference between max and min 'Speed'?

max_speed = pokemon_data['Speed'].max()
min_speed = pokemon_data['Speed'].min()
speed_difference = max_speed - min_speed

print(f'Max speed: {max_speed}')
print(f'Min speed: {min_speed}')
print(f'Speed dif: {speed_difference}')

# Filter the DataFrame to include only the Pokémon with 'Speed' >= 80.
# How many Pokémon meet this criterion?
# Display this DataFrame using your preferred visualization method.

fast_pokemons = pokemon_data[pokemon_data['Speed'] >= 80]
fast_pokemon_count = len(fast_pokemons)

print(f'Number of fast pokemons: {fast_pokemon_count}')

# Create a bar plot
plt.hist(fast_pokemons["Speed"], edgecolor = "black") 
plt.title("Pokemons with Speed >= 80")
plt.xlabel("Speed")
plt.ylabel("Frequency")
plt.show()

# (DIFFICULT) Find Pokémon with the longest name (excluding spaces)? What is this pokemons name?
longest_name_pokemon = pokemon_data.loc[pokemon_data['Name'].str.replace(' ', '').str.len().idxmax()]

print(f"Pokemon with the longest name: {longest_name_pokemon['Name']}")
