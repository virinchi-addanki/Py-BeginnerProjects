import random
max_num = 15
random_number = random.randint(1,max_num)
guess = 0
while guess!= random_number:
    guess = int(input(f"Guess the number between 1 & {max_num}:"))
    if guess<random_number:
        print("Wrong!Too Low );")
    elif guess>random_number:
        print("Wrong !Too High...):")
print(f"Wow!Nice guess (:")