from data_stored import data
from logo import logo, vs
import os
import random

def account_format(account):
    account_name = account["name"]
    account_disc = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_disc}, from {account_country}"

def check_answer(guess, a_follwers, b_followers):
    if a_follwers > b_followers:
        return guess == "a"
    else:
        return guess == "b"
print(logo)
score = 0
should_continue = True
account_b = random.choice(data)

while should_continue:
    account_a = account_b
    account_b = random.choice(data)
    while account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A : {account_format(account_a)}")
    print(vs)
    print(f"Againt B : {account_format(account_b)}")

    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    os.system('cls')
    print(logo)

    if is_correct:
        score += 1
        print(f"You're right! Current Score: {score}")
    else:
        should_continue = False
        print(f"Sorry, that's wrong, Final score: {score}")