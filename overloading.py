"""
TBSDrJ
Fall 2025
Because Python is both dynamically and weakly typed, it isn't great at
overloading.

Note: You could use type(user_input) == str below, but you shouldn't.  You
should get in the habit of using isinstance() instead because isinstance()
respects inheritance.  For ex, isinstance(user_input, object) will return True,
but type(user_input) == object will return False.  Sometimes, you want to
know if something *is* that type *exactly*, but, usually, you just want to know
if it behaves like a string or an integer, in which case you just need to know
if it inherits from string or integer or whatever.
"""

def choice_0(user_input: str | int) -> int:
    """Allow a user to select a choice using either an integer or a string."""
    if isinstance(user_input, str):
        # Handle string input
        print("User entered a string.")
    elif isinstance(user_input, int):
        # Handle integer input
        print("User entered an integer.")
    return 0 # Maybe return something more useful

def main():
    choice_0("a")
    choice_0(1)

if __name__ == "__main__":
    main()