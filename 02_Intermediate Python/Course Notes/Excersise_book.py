import numpy as np

store = np.array(['X', 'Z','Z','Z'])

cost = np.array([2,6,5,2])

select_cost = cost[store == 'X']

print(select_cost)
