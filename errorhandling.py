print("Learning programming with Lala")
# --- 1. ArithmeticError ---
# example of ArimethicError (specifically OverflowError)

import math

try:
    # Trying to calculate a factorial of a very large number might cause an Overflow
    # on some systems or with certain Python versions, especially with integers
    # However,Python's arbitrary precision integers make OverflowError for int operations rare
    # a more commmon example for OverflowError might involve floats:
    x = float('inf') * 2 # This might not raise OverflowError as 'inf' is already maxed out
    print(x)
except OverflowError as e:
    print(f"OverflowError occurred: {e}")
except ArithmeticError as e:
    print(f"ArithmeticError occurrred: {e}")
else:
    print("No ArithmeticError occurred, calculation successful.")

    # A clearer OverflowError for floats:
    # sys.float_info.max is the largest representable float
    # Multiplying it by 2 will often lead to infinity, but technically an overflow occurred.
    # To demonstrate a clear OverflowError, often one needs to be careful with contexts.

    # Let's try a different approach to trigger OverflowError with a mathematical function
    # that has limitations on its input range or output value.
    # Exponentiation can easily lead to OverflowError with floats.
    result = math.exp(1000) # e to the power of 1000 is a very large number
    print(f"Result: {result}")
except OverflowError:
print("Caught an OverflowError: The result of the operation is too large to be represented!")
except Exception as e:
print(f"An unexpected error occurred: {e}")

print("-" * 30)

try:
    denominator = 0
    result = 10 / denominator # This will raise ZeroDivisionError
    print(f"Result: {result}")
except ZeroDivisionError:
    print("Caught a ZeroDivisionError: Division by zero is not allowed")

# --- 2. ValueError and its Relatives ---
# Definition: Raised when an operation or function receives an argument that has the right type but an inappropriate value.
# Common Relatives/Situations leading to ValueError:
# Invalid Literals: Trying to convert a string that's not a valid number to an int or float
# Unpacking Issues: Trying to unpack a sequence with an incorrect number of elements
# Invalid Arguments to Functions/Methods: 
# any built-in functions or custom functions will raise ValueError
#  if an input value is outside an acceptable range.

# Example of ValueError:
try:
    num_str = "abc"
    num_int = int(num_str)
    print(f"Converted number: {num_int}")
except ValueError:
    print(f"Caught a ValueError: Cannot convert '{num_str}' to an integer.")

print("-" * 30)

try:
    # Trying to unpack an incorrect number of values
    a, b = [10]
    print(f"a: {a}, b: {b}")
except ValueError:
    print("Caught a ValueError: Not enough values to unpack!")

print("-" * 30)

try:
    my_list = [1,2,3]
    my_list.remove(4) # Trying to remove an element that doesn't exist
    print(my_list)
except ValueError:
    print("Caught a ValueError: value/element not found in list for remove operation!")

# ---- 3. TypeError ---
# TypeError: Raised when an operation or function is applied to an object of an inappropriate type
# ValueError is about the value, TypeError is about the type. They are often confused but distinct.

try:
    result = "hello" + 5 # Cannot concatenate string and integer
    print(result)
except TypeError:
    print("Caught a TypeError: Cannot concatenate string and integer!")

print("-" * 30)

try:
    len(5) # int has no len()
except TypeError:
    print("Caught a TypeError: 'int' object has no len()!")

# --- 4. IndexError ---
# IndexError: Raised when a sequence subscript (index) is out of range. This is often due to an "incorrect value" for an index.

my_list = [10, 20, 30]
try:
    item = my_list[3] # Index 3 is out of range/bounds
    print(f"Item: {item}")
except IndexError:
    print("Caught an IndexError: List index out of range!")

# --- 5.KeyError ---
# KeyError: Raised when a dictionary key is not found. Simillar to IndexError but for dictionaries.

my_dict = {"name": "Alice", "age": 30}
try:
    city = my_dict ["city"] # 'city' key does not exist
    print(f"City: {city}")
except KeyError:
    print("Caught a KeyError: Dictionary key not found!")

# --- 6. FleNotFoundError ---
# Raised when a file or directory is requested but doesn't exist. This is a common IOError (Input/Output Error).
try:
    with open("non_existent_file.txt", "r") as f:
        content = f.read()
        print(content)
except FileNotFoundError:
    print("Caught a FileNotFoundError: The file does not exist!")

# --- 7.NameError ---
# Raised when a local or global name is not found
# This typically happens when you try to use a variable or function before it has been defined.
try:
    print(undefined_variable) # This variable has not been defined
except NameError:
    print("Caught a NameError: The variable 'undefined_variale is not defined!")

#--- 8.AttributeError ---
# Raised when an attribute reference or assignment fails.
# This often means you're trying to access a method or property that doesn't exist on an object.

my_string = "Hello"
try:
    my_string.apped("world") # # Strings don't have an append method (lists do
except AttributeError:
    print("Caught an AttributeError: 'str' object has no attribute 'append'!")
    
# --- 9. ImportError
# Assume a module named 'non_existent_module' does not exist on your system
try:
    import non_existent_module
except ImportError as e:
    print(f"Caught an ImportError: {e}")
    print("Reason: The module 'non_existent_module' likely does not exist or isn't in Python's search path.")

print("\n--- Another example with a common typo ---")
try:
    # 'request' vs 'requests' - easy typo
    import request_library
except ImportError as e:
    print(f"Caught an ImportError: {e}")
    print("Reason: You might have intended to import 'requests' (plural) but typed 'request_library'.")

# --- 10. StopIteration ---
# Raised by the next() function and an iterator's __next__() method to signal that there are no further itemss
# produced by the iterator. This is usually handled internally by for loops, but can be caught explicitly.
