from game_data import data
import art
import random
# from replit import clear

def format_data(account):
    account_name = account['name']
    account_desc = account['description']
    account_count = account['country']
    return f"{account_name}, a {account_desc}, {account_count}"

def check_answer(guess,a_followers,b_followers):
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"
    
print(art.logo)
score = 0
game_should_continue = True
account_b = random.choice(data)

while game_should_continue:
    account_a = account_b
    account_b = random.choice(data)
    if account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A : {format_data(account_a)}.")
    print(art.vs)
    print(f"Against B: {format_data(account_b)}.")

    guess = input("Who has more followers? Type 'A' or 'B' : ").lower()

    a_followers_count = account_a['follower_count']
    b_followers_count = account_b['follower_count']
    is_correct = check_answer(guess,a_followers_count,b_followers_count)

    # clear()
    print(art.logo)
    if is_correct:
        score += 1
        print(f"You're right! Current Score : {score}.")
    else:
        game_should_continue = False
        print(f"Sorry, That's Wrong Final Score : {score}")
