# Jackpot game 
import random as rdm 

symboles = ["🍕", "🥨", "🥖", "🍥", "🍩", "🍪"]

# Choose the 3 symboles
def choose(symboles):
    s1 = rdm.choice(symboles)  
    s2 = rdm.choice(symboles)
    s3 = rdm.choice(symboles)
    return s1, s2, s3

# Compute gains from the bet
def compute_gains(s1, s2, s3, bet):
    if s1 == s2 == s3:
        print("!! JACKPOT !!")
        print(f"You win {bet * 5} coins !")
        return bet * 5
    elif s1 == s2 or s2 == s3 or s1 == s3:
        print("You got 2 same symboles.")
        print(f"You win {bet * 3} coins !")
        return  bet * 3
    else:
        print("You lost...")
        return 0

def level_two(symboles):
    return symboles + ["🥐", "🧀", "🥫", "🍙", "🥟", "🍣"]


# Display number of coins 
def play(coins):
    print("=========== COIN MACHINE ===========")
    print(f"Coins = {coins}")

coins = 100 
print("============= WELCOME TO THE COIN MACHINE =============")
level = input("Choose level 1 or level 2")

# ← ICI, avant le while
if level == "1":
    symboles = ["🍕", "🥨", "🥖", "🍥", "🍩", "🍪"]
elif level == "2":
    symboles = level_two(symboles)


# Game Loop
while True:
     bet_input = input("How much do you want to bet ? ")
     
     # Check for an int
     try:
        bet = int(bet_input)
     except ValueError:
        print("Enter a integer.")
        continue

     # Check for negative numbers 
     if bet < 0:
        print("It cannot be negative")
        continue

     # Check for limited input
     if bet > coins:
        print(f"You don't have enough coins ! Max bet: {coins}")
        continue 

     coins -= bet
     if bet != 0:
        symboles = level_two(symboles)
        s1, s2, s3 = choose(symboles)
        print(f"{s1}  {s2}  {s3}")
        gain = compute_gains(s1, s2, s3, bet)
        coins += gain
        play(coins)
        if coins == 0:
          print("YOU LOST --- NO COINS LEFT")
          break
     else:
        print("See you soon !")
        break

    