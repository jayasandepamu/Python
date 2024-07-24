import random
n=random.randrange(1,10)
guess=int(input('Enter any number  '))
if(guess<n):
        print('Too Low')
        guess=int(input('Enter number again  '))
elif(guess>n):
        print('Too high')
        guess=int(input('Enetr number again  '))
print('you guessed it right')
