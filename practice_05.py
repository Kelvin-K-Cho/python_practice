def multiply(array):
    squared = None
    for i in array:
        try:
            squared = i**2
        except:
            print("Array needs to contain integers.")
            break
        else:
            print(squared)

def divide(x, y):
    try:
        z = x/y
    except ZeroDivisionError as error:
        print(f"Cannot compute due to {error}")

# Test Cases:

# multiply(["a", "b", "c"])
# divide(1, 0)
