import random
import timeit

changeWins = 0
stayWins = 0
passes = 1000000

def montyHall(changeDoor):
    doorWithCar = random.randint(1, 3)
    guess = random.randint(1, 3)
    originalGuess = guess
    while True:
        doorWithoutCar = random.randint(1, 3)
        if doorWithoutCar != doorWithCar and doorWithoutCar != guess:
            break


    if changeDoor == True:
        while True:
            guess = random.randint(1, 3)
            if guess != doorWithoutCar and guess != originalGuess:
                break
    elif guess == doorWithoutCar:
        while True:
            guess = random.randint(1, 3)
            if guess != doorWithoutCar and guess != originalGuess:
                break
    #print(f"Original Guess: {originalGuess}\n Guess: {guess}\n Door with Car: {doorWithCar}\n Door without Car: {doorWithoutCar}")
    if guess == doorWithCar:
        return True
    else:
        return False

start = timeit.default_timer()

for i in range(1, passes+1):
    answer = montyHall(True)
    if answer:
        changeWins += 1
    print(f"Change Guess: {round(i/passes*100, 4)}%")

for i in range(1, passes+1):
    answer = montyHall(False)
    if answer:
        stayWins += 1
    print(f"Don't Change Guess: {round(i/passes*100, 4)}%")

end = timeit.default_timer()

print(f"Change Win Rate: {changeWins/passes*100}%")
print(f"Stay Win Rate: {stayWins/passes*100}%")
print(f"Time Elapsed: {end-start}")