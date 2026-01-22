#Task 7: Create a class Dog with a class variable species = "Canine". 
# Each object should also have its own name. 
# Demonstrate the difference by printing both.
#Task 8: Extend the Dog class with a counter (class variable) 
# that tracks how many dogs have been created so far.


class Dog:
    species = "Canine"
    # count = 0  # class variable counter

    def __init__(self, name):
        self.name = name
        # Dog.count += 1


dog1 = Dog("Buddy")
dog2 = Dog("Rocky")
dog3 = Dog("Max")

# print("Total dogs:", Dog.count)


print(dog1.name, "-", dog1.species)
print(dog2.name, "-", dog2.species)
