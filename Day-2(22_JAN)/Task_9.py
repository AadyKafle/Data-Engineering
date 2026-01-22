#Task 9: Create a class MathOps with:
        
# an instance method square(self, x)
# a classmethod cube(cls, x)
# a staticmethod is_even(x)


class MathOps:

    def square(self, x):
        return x * x

    @classmethod
    def cube(cls, x):
        return x * x * x

    @staticmethod
    def is_even(x):
        return x % 2 == 0

m = MathOps()

print(m.square(4))           # instance method
print(MathOps.cube(3))       # class method
print(MathOps.is_even(10))   # static method
