# Help with 80 character limit
# To set line in VSCode: Hit gear icon > Settings > search for 'ruler'
#   Select Editor: Rulers: 'Edit in settings.json' > Insert 80 in editor.rulers
#   list.  Save, and it should show up on-screen.

# Tip #1: Use parentheses to allow line breaks
# This will crash Python:
if my_really_long_variable_name == True and my_other_really_long_variable_name 
        == False:
# This will not:
if (my_really_long_variable_name == True and my_other_really_long_variable_name 
        == False):
# Same thing works in function definitions and formulas etc.

# If you have a really long print statement
# Just get the thought out:
print("I have a lot to say, and I'm really long-winded, and I'm gonna write a run-on sentence because no English teacher will ever read this.")
# Replace the print( with a variable:
my_str = "I have a lot to say, and I'm really long-winded, and I'm gonna write a run-on sentence because no English teacher will ever read this.")
# Make sections of this string as needed:
my_str = "I have a lot to say, and I'm really long-winded, and I'm gonna "
my_str += "write a run-on sentence because no English teacher will ever "
my_str += "read this."
# Add \n characters so the Terminal gets new lines too:
# You don't need an extra \n at the end
my_str = "I have a lot to say, and I'm really long-winded, and I'm gonna "
my_str += "write a \nrun-on sentence because no English teacher will ever "
my_str += "read this."
# Then print() that string
my_str = "I have a lot to say, and I'm really long-winded, and I'm gonna "
my_str += "write a \nrun-on sentence because no English teacher will ever "
my_str += "read this."
print(my_str) # print() ends with a newline character by default

# Annotations:
# If your parameter could have more than one data type use OR symbol | :
def my_function(my_var: str | None) -> int | None:

# If you are annotating a class that hasn't been defined yet: put it in quotes
def my_function(my_var: 'MyClass'):

# Docstrings:
# Still gotta follow 80 character limit, and, if there's more than one line,
#   then put a blank line after the first line.
def my_function() -> None:
    """This is what my function does, briefly.
    
    Here's some more information about my function."""