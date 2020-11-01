def f(x):
    """
    Returns float(x).
    :param x: int.
    :return : floatof x.
    """
    try:
        return float(x)
    except ValueError:
        print("Invalid input.")

c = f(3)
print(c)
