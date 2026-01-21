#Function
#take a list as input
def find_max(lst):
    maximum = lst[0]
    for num in lst:
        if num > maximum:
            maximum = num
    return maximum


#GCD divisor
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
