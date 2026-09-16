# Task: Dictionary Frequency Mapping
# Instructions: Return a dictionary where keys are categories 
# and values are the count of occurrences.

def count_categories(categories):
    thisdict = {}

    for x in categories:
        if x in thisdict:
            thisdict[x] += 1
        else:
            thisdict[x] = 1

    return thisdict


data = ['Brakes', 'Engine', 'Brakes', 'Tools', 'Engine', 'Brakes']

# Expected: {'Brakes': 3, 'Engine': 2, 'Tools': 1}
print(count_categories(data))
