"""
We did all these examples on the board on Weds 9/24.

Mostly, you should think of "positional" as being the same as "required" and
"keyword" as being the same as "optional."  But, this shows examples of when
those correspondances can be violated.
"""

# This is actually valid Python, but kinda weird.
def f(a, /, b, *, c):
    """This is weird because c must be provided as a keyword argument, so it 
    should be a keyword parameter."""
    print(f"{a=}, {b=}, {c=}")

print("\nUsing def f(a, /, b, *, c):\n")
# Possible calls:
try:
    f(1, 2, 3)
except TypeError as e:
    print("f(1, 2, 3) is not a valid function call because:")
    print(f"TypeError: {e}")
# You can do these, they all result in a=1, b=2, c=3:
print("f(1, 2, c=3) is valid, and yields: ", end="")
f(1, 2, c=3) 
print("f(1, b=2, c=3) is valid, and yields: ", end="")
f(1, b=2, c=3)
print("f(1, c=3, b=2) is valid, and yields: ", end="")
f(1, c=3, b=2)
try:
    f(a=1, b=2, c=3)
except TypeError as e:
    print("f(a=1, b=2, c=3) is not a valid function call because:")
    print(f"TypeError: {e}")

print("\n\nUsing def g(a=None, /, b=None, *, c=None):\n")

# This is also valid Python, but also a little weird.
def g(a=None, /, b=None, *, c=None):
    """This is weird because a must be provided as a positional argument, but
    it is a keyword parameter."""
    print(f"{a=}, {b=}, {c=}")

print("g(5) is valid, and yields: ", end="")
g(5)
try:
    g(a=5)
except TypeError as e:
    print("g(a=5) is not a valid function call because:")
    print(f"TypeError: {e}")
try:
    g(5, 6, 7)
except TypeError as e:
    print("g(5, 6, 7) is not a valid function call because:")
    print(f"TypeError: {e}")
# g(c=7, 5, 6)
print("g(c=7, 5, 6) is not a valid Python syntax because:")
print(f"SyntaxError: positional argument follows keyword argument")
print("g(5, 6, c=7) is valid, and yields: ", end="")
g(5, 6, c=7)
print("g(5, c=7, b=6) is valid, and yields: ", end="")
g(5, c=7, b=6)
print("g(5, 6) is valid, and yields: ", end="")
g(5, 6)
print("g(b=5, c=6) is valid, and yields: ", end="")
g(b=5, c=6)