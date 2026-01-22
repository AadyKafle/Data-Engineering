#Task2: Write a Laptop class with attributes brand and price.
# Create 3 objects and store them in a list.
# Print the list in a readable way (e.g., Dell - $800)

class Laptop:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    def display(self):
        print(f"{self.brand} - ${self.price}")

laptop1 = Laptop("Dell", 800)
laptop2 = Laptop("HP", 750)
laptop3 = Laptop("Apple", 1200)

laptops = [laptop1, laptop2, laptop3]
for laptop in laptops:
    laptop.display()
