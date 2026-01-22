#Task 5: Write a class DataSize with init, str, and 
# add so you can add two DataSize objects and print them nicely.

class DataSize:
    def __init__(self, size):
        self.size = size  # size in MB

    def __add__(self, other):
        return DataSize(self.size + other.size)

    def __str__(self):
        return f"{self.size} MB"

d1 = DataSize(500)
d2 = DataSize(300)

d3 = d1 + d2 # bhitra : d3 = d1.__add__(d2)
print(d3) #bhitra yesari kaam garchha : print(d3.__str__())
