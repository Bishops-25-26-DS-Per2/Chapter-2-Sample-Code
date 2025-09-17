c = 11
d = 73

def f(x):
    global d
    c = 23
    print(f"{x=}, {c=}, {d=}")
    print(f"{locals()=}, {globals()=}")
    d = 59
    print(f"{x=}, {c=}, {d=}")

def main():
    a = 5
    f(a)
    print(f"{locals()=}, {globals()=}")

main()
f(c)
f(d)
print(f"{x=}, {c=}, {d=}")
print(f"{locals()=}, {globals()=}")
