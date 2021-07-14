import random
print('Hello. What is your name?')
name = input()

print('Well, ' + name + ', I am thinking of a number between 1 and 20')
secret_number = random.randint(1, 20)
for guess_taken in range(1, 7):
    pass
print('You took' + str(guess_taken) + ' guesses.')