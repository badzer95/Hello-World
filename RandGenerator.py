import random
def RandomGenerator(x:int,y:int):
    return random.randint(x,y)
def DigitChecker(x):
    if x.isdigit():
        return True
    else:
        print("Your input is invalid.")
        return False
def InputChecker(x,y,z):
    #x is user input; y is lower bound; z is upper bound
    if not DigitChecker(x):
        return False
    elif int(x) >= y and int(x) <= z:
        return True
    else:
        print("Your input is invalid.")
        return False
loop = True
while loop:
    iterator = input("Enter the number of random numbers to be generated: ")
    while not DigitChecker(iterator):
        iterator = input("Enter the number of random numbers to be generated: ")
        DigitChecker(iterator)
    iterator = int(iterator)
    counter = 0 
    lowerBound = input("Enter the lower bound number: ")
    while not DigitChecker(lowerBound):
        lowerBound = input("Enter the lower bound number: ")
        DigitChecker(lowerBound)
    lowerBound = int(lowerBound)
    upperBound = input("Enter the upper bound number: ")
    while not DigitChecker(upperBound):
        upperBound = input("Enter the upper bound number: ")
        DigitChecker(upperBound)
    upperBound = int(upperBound)
    while counter < iterator:
        numRand = RandomGenerator(lowerBound, upperBound)
        counter += 1
        print(f"Random number {counter}: {numRand}")
    print("Enter 0 to end the program")
    print("Enter 1 to generate more random numbers")
    loop = input("Enter 0 or 1: ")
    while not InputChecker(loop, 0, 1):
        loop = input("Enter 0 or 1: ")
    loop = bool(int(loop))