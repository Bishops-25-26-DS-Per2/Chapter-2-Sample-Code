def f(x, y = 5):
    # x is position and required
    # y is keyword and optional
    # Possible valid calls:
    # f(1)  Then: x=1, y=5
    # f(1, 3)   Then: x=1, y=3
    # f(x=1, y=3)   Then: x=1, y=3
    # f(y=3, x=1)   Then: x=1, y=3
    # INVALID calls:
    # f(y=3, 1)   Then: 1 is in the wrong position
    # f(1, 2, 3)   Then: too many inputs
    # f()   Then: Not enough inputs
    print(f"{x=}, {y=}")

def g(*args):
    # Then all inputs are in a tuple called args
    # g(1)   Then: args = (1); len(args) = 1
    # g(1, 2)   Then: args = (1, 2); len(args) = 2
    # g()   Then: args = (); len(args) = 0
    # g((1, 2, 3))   Then: args = ((1, 2, 3)) len(args) = 1
    # INVALID calls:
    # g(y=5)   Then: It doesn't know what y is.
    print(f"{args=}, {len(args)=}")

def h(**kwargs):
    # h(y=5)   Then: kwargs = {'y': 5}, and there is 1 key-value pair.
    # h(x=1, y=5)   Then: kwargs = {'x': 1, 'y': 5} and there are 
    #                   2 key-value pairs.
    # INVALID calls:
    # h(5)   Then: h takes zero positional arguments, it doesn't know where
    #           to put that value of 5.
    print(f"{kwargs=}, {kwargs.keys()=}, {kwargs.values()=}")
    print(f"\t{len(kwargs)=}, {len(kwargs.keys())=}, {len(kwargs.values())=}")

def main():
    print("f(1): ", end="")
    f(1)
    print("f(1, 3): ", end="")
    f(1,3)
    print("f(x=1, y=3): ", end="")
    f(x=1, y=3)
    print("f(y=3, x=1): ", end="")
    f(y=3, x=1)
    # f(y=3, 1)  Python won't let me include this, even inside of a try/except, 
    #                   because it is considered to be a Syntax Error.
    try:
        f(1,2,3)
    except:
        print("f(1,2,3) is invalid.")
    try:
        f()
    except:
        print("f() is invalid.")
    print("g(1): ", end="")
    g(1)
    print("g(1, 2): ", end="")
    g(1, 2)
    print("g(): ", end="")
    g()
    print("g((1, 2, 3)): ", end="")
    g((1, 2, 3))
    try:
        g(y=5)
    except:
        print("g(y=5) is invalid.")
    print("h(y=5): ", end="")
    h(y=5)
    print("h(x=1, y=5): ", end="")
    h(x=1, y=5)
    try:
        h(5)
    except:
        print("h(5) is invalid.")

if __name__ == "__main__":
    main()