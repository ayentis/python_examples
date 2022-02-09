def read_int(prompt, min, max):

    v = int(input(prompt))
    assert min <= v <= max
    return v

while True:
    try:
        v = read_int("Enter a number from -10 to 10: ", -10, 10)
        break
    except ValueError:
        print("Error: wrong input try again")
    except AssertionError:
        print("Error: the value is not within permitted range (min..max)")

print("The number is:", v)