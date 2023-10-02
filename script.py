import random

w = ["apple", "banana", "cherry", "dog", "elephant", "flamingo", "giraffe", "hamburger", "iguana", "jacket"]

def a():
    return random.choice(w)

def b():
    x = a()
    y = []
    z = 6
    return x, y, z

def c(x, y):
    d = ""
    for e in x:
        if e in y:
            d += e
        else:
            d += "_"
    return d

def f():
    while True:
        g = input("Guess a letter: ").lower()
        if len(g) != 1 or not g.isalpha():
            print("Please enter a single letter.")
        else:
            return g

def h():
    x, y, z = b()

    while z > 0:
        print("\nAttempts left:", z)
        print("Current word:", c(x, y))

        g = f()

        if g in y:
            print("You've already guessed that letter.")
        elif g in x:
            y.append(g)
            if c(x, y) == x:
                print("Congratulations! You guessed the word:", x)
                break
        else:
            y.append(g)
            z -= 1

    if z == 0:
        print("\nYou ran out of attempts. The word was:", x)


