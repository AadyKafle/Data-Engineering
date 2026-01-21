#dict problem 1
#: Write a function that takes a list of dictionaries as input, where 
# each dictionary represents a person with keys 'name' and 'age',
# and returns a new dictionary where the keys are the ages
# and the values are lists of names that correspond to that age.

def group_by_age(people):
    result = {}
    for person in people:
        age = person['age']
        name = person['name']
        if age not in result:
            result[age] = []
        result[age].append(name)
    return result


#Dictionary Problem 2

def word_frequency(s):
    freq = {}
    for word in s.split():
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1
    return freq
