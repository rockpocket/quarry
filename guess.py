import sys

secret = 7

guess = input("what's you're guess?")

guess = int(guess)

if (guess < secret):
    print("Too low, fuck-o")
elif (guess > secret):
    print("Too high, smart guy")
elif (guess == secret):
    print("accuarate and immaculate")

sys.exit(0) > None