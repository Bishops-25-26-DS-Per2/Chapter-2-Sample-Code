PI=3.14159265368979

# If I just use the typical way of taking arguments, for ex:
def cos(x: float) -> float:
    """Find the cos(x), where x is in radians."""
    ...

# Then I can call this function either using:
# Positional argument
cos(PI/2)
# or
# Keyword argument
cos(x = PI/2)

# HOWEVER, if you do what the Python Math library does:
def cos(x: float, /) -> float:
    ...

# Then I can ONLY provide x as a positional argument, so:
cos(PI/2) # No problem
cos(x=PI/2) # Python will crash

# The reason the math library does this is to interface with C.

# If you include a * as an argument all by itself, everything that follows
#   must be provided as a keyword argument (c.f. math.isclose)
def is_close(x, y, *, rel_tol=0.1e-09, abs_tol=0.0) -> bool:
    ...

# You can combine / and *:
def is_close(x, y, /, *, rel_tol=0.1e-09, abs_tol=0.0) -> bool:
    ...

# In this case, x, y are required positional arguments that have to provided
#   positionally, and rel_tol abs_tol are optional arguments that have to
#   be provided as keyword arguments.
# You can have arguments between that could be provided either as positional
#   or keyword arguments. 

# See exec() function in Python 3.12 or earlier for optional positional 
#   parameters:
# exec(source, globals=None, locals=None, /, *, closure=None)

# But in Python 3.13+ globals and locals become either positional or keyword:
# exec(source, /, globals=None, locals=None, *, closure=None)