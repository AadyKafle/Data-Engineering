#List Problem 1
#Product of all elements except itself
def product_except_self(lst):
    result = []
    for i in range(len(lst)):
        product = 1
        for j in range(len(lst)):
            if i != j:
                product *= lst[j]
        result.append(product)
    return result

#List problem 2: Write a function that takes two lists as input
# and returns a new list containing the elements that are common to both lists.

def common_elements(a, b):
    return list(set(a) & set(b))
