amount = 5
iterations = 2

try:
    average = amunt / iterations
except ZeroDivisionError:
    print("You can't divide by zero")
finally:
    print(average)