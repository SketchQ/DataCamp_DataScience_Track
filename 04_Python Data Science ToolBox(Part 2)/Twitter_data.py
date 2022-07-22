'''
In this exercise, you will do just that. 
You will process a large csv file of Twitter data in the same way that you processed 
'tweets.csv' in Bringing it all together exercises of the prequel course, but this time,
 working on it in chunks of 10 entries at a time.
'''

import pandas as pd

df = pd.read_csv('DataSets\\tweets.csv')

# Initialize an empty dictionary: counts_dict
counts_dict = {}

# Iterate over the file chunk by chunk
for chunk in pd.read_csv('DataSets\\tweets.csv', chunksize=10):

    # Iterate over the column in DataFrame
    for entry in chunk['lang']:
        if entry in counts_dict.keys():
            counts_dict[entry] += 1
        else:
            counts_dict[entry] = 1

# Print the populated dictionary
print(counts_dict)

print('\n-----------------------------------------------------\n')

'''
Extracting information for large amounts of Twitter data:
In this exercise, you will be making your code more reusable by putting your work 
in the last exercise in a function definition.
'''

# Define count_entries()
def count_entries(csv_file, c_size, colname):
    """Returns a dictionary with counts of occurences as value for each key."""

    # Initialize an empty dictionary: counts_dict
    counts_dict = {}

    # Iterate over the file chunk by chunk
    for chunk in pd.read_csv(csv_file, chunksize=c_size):

        # Iterate over the column in DataFrame
        for entry in chunk[colname]:
            if entry in counts_dict.keys():
                counts_dict[entry] += 1
            else:
                counts_dict[entry] = 1

    # Return counts_dict
    return counts_dict

# Call count_entries(): result_counts
result_counts = count_entries('DataSets\\tweets.csv', 10, 'lang')

# Print result_counts
print(result_counts)

print('\n-----------------------------------------------------\n')

'''
List comprehensions for time-stamped data

In this exercise, you will be using a list comprehension to extract the time 
from time-stamped Twitter data.
'''

# Extract the created_at column from df: tweet_time
tweet_time = df['created_at']

# Extract the clock time: tweet_clock_time
tweet_clock_time = [entry[11:19] for entry in tweet_time]

# Print the extracted times
print(tweet_clock_time)


print('\n-----------------------------------------------------\n')

'''
Conditional list comprehensions for time-stamped data

In this exercise, you will be using a list comprehension to extract the time from time-stamped
Twitter data. You will add a conditional expression to the list comprehension so that you only
select the times in which entry[17:19] is equal to '19'

'''

# Extract the created_at column from df: tweet_time
tweet_time = df['created_at']

# Extract the clock time: tweet_clock_time
tweet_clock_time = [entry[11:19] for entry in tweet_time if entry[17:19] == '19']

# Print the extracted times
print(tweet_clock_time)
