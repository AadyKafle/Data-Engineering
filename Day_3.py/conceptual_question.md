# 1. What is a recursive function, and how does it differ from an iterative solution?

A recursive function is a function that calls itself to solve a problem. It breaks a big problem into smaller versions of the same problem.

An iterative solution solves the problem using loops like for or while instead of function calls.

Key differences:

Recursion uses function calls and the call stack.

-Iteration uses loops and variables.

-Recursion is often more readable for problems like tree traversal.

-Iteration is usually more memory-efficient.

# 2. Why is it important to have a base case in a recursive function?

A base case is the condition that stops the recursion.

Without a base case:

The function will keep calling itself forever.

This leads to a stack overflow error.

The base case tells Python when to stop and start returning results.

# 3. What is a context manager in Python?

A context manager is an object that manages resources automatically.

It ensures that:

A resource is properly set up before use.

The resource is properly cleaned up after use.

Common examples include files, database connections, and network connections.

# 4. What is the purpose of the with statement in Python?

The with statement is used to work with context managers.

Its purpose is to:

Simplify resource management.

Automatically handle setup and cleanup.

Reduce errors caused by forgetting to close resources.

# 5. How does the with statement help in managing resources like files or network connections?

When using with:

The resource is opened at the start.

The resource is automatically closed, even if an error occurs.

This makes code:

Safer

Cleaner

Easier to read

# 6. What is the role of the __enter__ and __exit__ methods in a context manager?

__enter__() runs when the with block starts.

__exit__() runs when the with block ends.

How they work together:

__enter__() prepares the resource.

The code inside with executes.

__exit__() cleans up the resource, even if an exception occurs.

# 7. What are the different file modes in Python?

Common file modes include:

r : Read (file must exist)

w : Write (creates or overwrites file)

a : Append (adds data to end of file)

rb : Read binary

wb : Write binary

Binary modes are used for files like images, audio, and videos.

# 8. What is the difference between read(), readline(), and readlines()?

read()
Reads the entire file as one string.

readline()
Reads one line at a time.

readlines()
Reads all lines and returns them as a list of strings.

# 9. What is a CSV file, and why is it widely used?

A CSV (Comma-Separated Values) file stores data in tabular form using commas.

It is widely used because:

It is simple and lightweight.

It is supported by many tools (Excel, databases, Python, etc.).

It is easy to read and write.

# 10. How does Python’s csv module help in reading and writing CSV files?

The csv module:

Handles reading and writing CSV files correctly.

Manages delimiters, quotes, and newlines.

Prevents common formatting mistakes.

It makes CSV handling reliable and platform-independent.

# 11. What is JSON, and how is it different from Python dictionaries?

JSON (JavaScript Object Notation) is a text-based data format.

Differences from Python dictionaries:

JSON uses only basic data types.

JSON keys must be strings.

JSON is language-independent.

Python dictionaries can store complex Python objects.

# 12. Why is JSON preferred for data exchange in web APIs?

JSON is preferred because:

It is lightweight and fast to transmit.

It is easy to read for humans and machines.

It is supported by almost all programming languages.

It works naturally with web technologies.