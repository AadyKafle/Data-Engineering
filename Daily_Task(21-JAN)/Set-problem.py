#Set Problem 1
#Elements in first list but not in second

def difference_set(list1, list2):
    return set(list1) - set(list2)


#Set Problem 2
#Unique characters from list of strings
def unique_characters(strings):
    result = set()
    for word in strings:
        for char in word:
            result.add(char)
    return result