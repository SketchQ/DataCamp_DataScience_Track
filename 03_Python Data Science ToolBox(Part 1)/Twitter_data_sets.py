'''
For this exercise, your goal is to recall how to load a dataset into a DataFrame. 
The dataset contains Twitter data and you will iterate over entries in a column to build a 
dictionary in which the keys are the names of languages and the values are the number of 
tweets in the given language. The file tweets.csv is available in your current directory.
'''

# Import pandas
import pandas as pd

# Import Twitter data as DataFrame: df
df = pd.read_csv('DataSets\\tweets.csv')

# Initialize an empty dictionary: langs_count
langs_count = {}

# Extract column from DataFrame: col
col = df['lang']

# Iterate over lang column in DataFrame
for entry in col:
    
        # If the language is in langs_count, add 1
        if entry in langs_count.keys():
            langs_count[entry] += 1
        # Else add the language to langs_count, set the value to 1
        else:
            langs_count[entry] = 1

# Print the populated dictionary
print(langs_count)


print('\n-----------------------------------------------------\n')

'''
In this exercise, you will define a function with the functionality you developed in the
 previous exercise, return the resulting dictionary from within the function, 
 and call the function with the appropriate arguments.
'''

# Define count_entries()
def count_entries(df, col_name='lang'):
    """Return a dictionary with counts of
    occurrences as value for each key."""

    # Initialize an empty dictionary: lang_count
    lang_count = {}
   
    # Extract column from DataFrame: col
    col = df[col_name]

    # Iterate over lang column in DataFrame
    for entry in col:

        # If the language is in lang_count, add 1
        if entry in lang_count.keys():
            lang_count[entry] += 1

        # Else add the language to lang_count, set the value to 1
        else:
            lang_count[entry] = 1
        
    # Return the lang_count dictionary
    return lang_count
    

# Call count_entries(): result1
result1 = count_entries(df, 'lang')

# Print result1
print(result1)