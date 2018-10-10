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

def ask():
    response = None
    squared = None
    while not squared:
      response = input("Input an integer: ")
      try:
        int(response)
      except:
        print("An error occured!  Please try again!")
      else:
        squared = int(response)**2
        print(f"Thank you, your number squared is : {squared}")


# Test Cases:

# multiply(["a", "b", "c"])
# divide(1, 0)
ask()
