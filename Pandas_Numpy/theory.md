1️⃣ What is NumPy and why is it preferred over Python lists?

NumPy (Numerical Python) is a library for fast numerical computing in Python.
It provides powerful array objects and mathematical functions.

Why preferred over Python lists?
Python List	NumPy Array
Stores mixed data types	Stores single data type
Slower for math operations	Very fast (C optimized)
No vectorized operations	Supports vectorization
High memory usage	Memory efficient
Example:
# Python list
a = [1, 2, 3]
b = [4, 5, 6]
result = [a[i] + b[i] for i in range(len(a))]
# NumPy
import numpy as np
a = np.array([1,2,3])
b = np.array([4,5,6])
result = a + b

NumPy is faster because operations run in optimized C code internally.

2️⃣ What is ndarray?

ndarray = N-dimensional array object in NumPy.

import numpy as np
arr = np.array([[1,2,3],[4,5,6]])
Difference from Python list:

Fixed data type

Fixed size

Stored in contiguous memory

Supports vectorized math

Python lists store pointers to objects; ndarray stores raw data in memory.

3️⃣ What is Vectorization?

Vectorization = performing operations on entire arrays at once without writing loops.

a = np.array([1,2,3])
b = a * 2   # vectorized

Instead of:

for i in range(len(a)):
    a[i] *= 2
Why faster?

No Python loop overhead

Uses optimized C backend

CPU-level optimizations (SIMD)

4️⃣ What is Broadcasting?

Broadcasting allows NumPy to operate on arrays of different shapes.

Example:

a = np.array([[1,2,3],
              [4,5,6]])

b = np.array([10,20,30])

print(a + b)

Output:

[[11 22 33]
 [14 25 36]]

Here, b is stretched across rows automatically.

📌 Useful in:

Adding bias in neural networks

Scaling datasets

5️⃣ reshape() vs resize()
reshape()

Returns new view (if possible)

Does not modify original array

a = np.array([1,2,3,4])
b = a.reshape(2,2)
resize()

Modifies original array

Can change size

a.resize(2,2)
6️⃣ What are ufuncs?

Universal functions (ufuncs) are element-wise operations.

Examples:

np.add()
np.subtract()
np.sqrt()
np.exp()

Example:

np.sqrt(np.array([1,4,9]))
7️⃣ Shallow Copy vs Deep Copy
a = np.array([1,2,3])
b = a          # reference
c = a.view()   # shallow copy
d = a.copy()   # deep copy

Shallow copy shares data.

Deep copy duplicates memory.

Changing a affects c but not d.

8️⃣ Indexing in Multi-dimensional arrays
a = np.array([[1,2,3],
              [4,5,6]])

a[0] → first row

a[0,1] → element 2

a[:,1] → second column

9️⃣ axis parameter

Axis defines direction of operation.

a.sum(axis=0)  # column-wise
a.sum(axis=1)  # row-wise

axis=0 → down rows
axis=1 → across columns

🔟 NumPy Memory Storage

NumPy:

Contiguous memory block

Fixed dtype

Faster cache access

Python list:

Stores references

Non-contiguous

More memory overhead

📊 PANDAS
1️⃣ What is Pandas?

Pandas is built on NumPy for data analysis.

NumPy → numerical arrays

Pandas → labeled data tables

2️⃣ Series and DataFrame
Series

1D labeled array

s = pd.Series([10,20,30])
DataFrame

2D table

df = pd.DataFrame({
    "A":[1,2],
    "B":[3,4]
})
3️⃣ loc vs iloc
loc	iloc
Label-based	Position-based
df.loc[0]      # by label
df.iloc[0]     # by index
4️⃣ merge vs join vs concat

merge() → SQL-style join

join() → index-based join

concat() → stack DataFrames

5️⃣ Missing values

Represented as:

NaN

None

Functions:

df.isna()
df.fillna()
df.dropna()
6️⃣ groupby()

Used for aggregation.

df.groupby("Department")["Salary"].mean()
7️⃣ apply() vs map()

map() → element-wise (Series only)

apply() → row/column-wise

8️⃣ MultiIndex

Hierarchical indexing:

df.set_index(["State","City"])
9️⃣ Pivot Table

Summarizes data:

pd.pivot_table(df,
               values="Sales",
               index="Region",
               columns="Year",
               aggfunc="sum")
🔟 Time Series
df['date'] = pd.to_datetime(df['date'])
df.set_index('date')

Supports:

resample()

rolling()

shift()

🔥 ADVANCED NUMPY
np.copy() vs =

= → reference
np.copy() → deep copy

Structured arrays

Arrays with named fields:

dtype = [('name','U10'), ('age','i4')]

Used like mini database rows.

Strides

Strides = number of bytes to move in memory to go next element.

Helps NumPy move efficiently through array.

C-order vs Fortran-order

C-order → row-major

Fortran-order → column-major

np.where()
np.where(a > 5)

Returns indices.

Boolean indexing:

a[a>5]
Fancy indexing
a[[0,2]]

Select specific indices.

np.einsum()

Einstein summation notation.

Example matrix multiplication:

np.einsum('ij,jk->ik', A, B)

Used in deep learning, physics.

stack vs hstack vs vstack

stack() → new axis

hstack() → horizontal

vstack() → vertical

Masked arrays

Handle invalid data:

np.ma.masked_array(a, mask=[0,1,0])
Integer overflow

NumPy:

np.array([250], dtype=np.uint8) + 10

Wraps around (overflow).

Python:

250 + 10

No overflow (big integers).

🔥 ADVANCED PANDAS
copy() vs view & SettingWithCopyWarning

Sometimes slicing returns a view.

Modifying it can cause warning:

SettingWithCopyWarning

Better:

df.loc[:, 'col'] = value
Method chaining
(df
 .dropna()
 .groupby("A")
 .mean())

Cleaner but harder to debug.

stack vs unstack

stack() → columns → rows

unstack() → rows → columns

explode()

Splits list elements into rows.

df.explode("column")
transform vs agg

agg() → reduces size

transform() → keeps same size

cut vs qcut

cut() → equal width bins

qcut() → equal frequency bins

Memory optimization

Use categorical dtype

Downcast integers

Use chunking

Use .astype()

ffill vs bfill

ffill() → forward fill

bfill() → backward fill

pd.Categorical

Used for repeated string values.

Improves:

Memory usage

Groupby performance

resample vs rolling

resample() → change frequency

rolling() → moving window calculation

Example:

df.resample('M').mean()
df.rolling(7).mean()