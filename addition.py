def add(a,b):
    return a+b
if __name__== "__main__":
    import sys
    if len(sys.argv) == 3:
        script_name = sys.argv[0]
        x=int(sys.argv[1])
        y=int(sys.argv[2])
    else:
        x=10
        y=20 

    print("The sum is: ", add(x, y))
