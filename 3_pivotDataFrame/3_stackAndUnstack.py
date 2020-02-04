import pandas as pd

trials = pd.read_csv('/Users/apple/desktop/manipulatingDataFrames/dataset/trials_01.csv')

print(trials)
trials = trials.set_index(['treatment', 'gender'])
print(trials) # NOTE: pivot cant work because of multi index

# unstack a multi-index(1)
unstack = trials.unstack(level='gender') # NOTE: level refers to the layer of index, here we unstack 1 layer
print(unstack)

# unstack a multi-index(2) | the result is the same as above
trial_by_gender = trials.unstack(level=1)
print(trial_by_gender)

# stack: make a wide df thinner and longer
print(trial_by_gender.stack(level='gender')) # NOTE: gender level is the innermost level
# NOTE: the result is the same as when we set_index()

# swaplevel() method: swap the inner and outer index level
stacked = trial_by_gender.stack(level='gender')
swapped = stacked.swaplevel(0,1) # NOTE: swap the first and second level
print(swapped)

sorted = swapped.sort_index()
print(sorted)
