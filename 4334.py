def f(a,b):
    try:
        
        a = int(a)
        b = int(b)
        print(a/b)
    except(ZeroDivisionError, ValueError):
        print("INvalid Error")
