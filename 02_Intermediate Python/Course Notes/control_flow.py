# Control Flow - DataCamp-Python

print('-----If-elif-else-----')

z = 6

if z % 2 == 0:
    print('z is divisible by 2') # This will print

elif z % 3 == 0 :
    print('z is divisible by 3') # This will not print

else :
    print('z is not divisible by 2 or 3')

# Moving on

print('-----While-loop-----')

error = 50.0
while error > 1 : #True
    error = error / 4
    print(error)

#Inverted pendulum
print('-----Inverted Pendulum-----')
offset = -6

while offset != 0:
    print('correcting...')
    if offset > 0:
        offset = offset - 1
    else:
        offset = offset + 1
    print(offset)


print('-----For-loop-----')

#Syntax: for <variable> in <sequence>:

fam = [1.73, 1.68, 1.71, 1.89]

for height in fam:
    print(height)

# Enumerate
print('-----Enumerate-----')

for index, height in enumerate(fam):
    print('index '+ str(index) + ': ' + str(height))

# For loop over a string
print('-----For loop over a string-----')

for c in 'Family':
    print(c)

# Loop over list of lists
print('-----Loop over list of lists-----')

house = [['hallway', 11.25],
         ['kitchen', 18.0], 
         ['living room', 20.0], 
         ['bedroom', 10.75], 
         ['bathroom', 9.50]]

for room in house:
    print('the ' + room[0] + ' is ' + str(room[1]) + ' sqm')

## Loop Structures
print('-----Loop Structures-----')

print('-----Loop over dictionary-----')

world = {'afghanistan':30.55, 
        'albania':2.77, 
        'algeria':39.21}

for key,value in world.items():
    print(key + ': ' + str(value))


# Numpy Arrays
print('-----Numpy Arrays-----')

import numpy as np

np_height = np.array([1.73, 1.68, 1.71, 1.89, 1.80])
np_weight = np.array([ 65.4, 59.2, 63.6, 88.4, 68.7])
bmi = np_weight / np_height ** 2

for val in bmi:
    print(val)

meas = np.array([np_height,np_weight])

for i in meas: 
    print(i) # This will print the arrays itself

print('-----Numpy Arrays[nditer() METHOD]-----')
for val in np.nditer(meas):
    print(val) # This will print first the height and then the weight

## Looping Over Panda DataFrames
print('-----Looping Over Panda DataFrames-----')

import pandas as pd

cars = pd.read_csv('Resources\cars.csv', index_col=0)
brics = pd.read_csv('Resources\\brics.csv', index_col=0)

# Non-convient way
for car,row in cars.iterrows():
    print(car)
    print(row)

# Convient way
for lab,row in cars.iterrows():
    print(str(lab) + ': ' + str(row['cars_per_cap']))

# Adding a column

for lab,row in brics.iterrows() :
    brics.loc[lab, "name_length"] = len(row["country"])

print(brics)

print("\n-------------------------------------\n")

for lab,row in cars.iterrows() :
    cars.loc[lab, "COUNTRY"] = row["country"].upper()

print(cars)

print("\n-------------------------------------\n")
print('apply() METHOD\n')
# Easier way to add a column is using the apply() method

brics["name_length"] = brics["country"].apply(len)

print(brics)

print("\n-------------------------------------\n")

cars["COUNTRY"] = cars["country"].apply(str.upper)

print(cars)
