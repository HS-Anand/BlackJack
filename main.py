import random

import os


clear = lambda: os.system('cls')

def cards_sum(cards):
  sum = 0
  for i in cards:
    sum += i
  return sum


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
end = False
amount = 1000
high = 1000
win_count = 0
insure_bet = 0
insurance_bet = 0


def insurance(comp, cond):
  insurance_bet = 0
  if comp[0] == 11:
    print(f"Dealer's first card: {comp[0]}\n")
    insure = input("Do you want to buy insurance?\nYes/No:  ").lower()
    print("\n")
    if insure == "yes":
      insure_bet = int(input("Enter insurance bet: "))
      cond = cond - insure_bet
      if cond < 0:
        print("You don't have enough money to play insurance")
        print("\n")
      else:
        if comp[1] == 10:
          print("You won insurance\nPlease continue\n")
          insurance_bet = int(insure_bet * 2)
        else:
          print("Not a blackjack\nYou lost insurance\nPlease continue\n")
          insurance_bet = int(insure_bet * -1)
  return insurance_bet


while not end:
  stand = False
  win = False
  push = False
  user = []
  comp = []

  user.append(random.choice(cards))
  user.append(random.choice(cards))
  comp.append(random.choice(cards))
  comp.append(random.choice(cards))

  # BlackJack

  blackjack = False
  blackjack_user = False
  if cards_sum(user) == 21:
    if cards_sum(comp) == 21:
      stand = True
      push = True
    else:
      blackjack_user = True
      stand = True
  blackjack_comp = False
  if cards_sum(comp) == 21:
    blackjack_comp = True

  if blackjack_user or blackjack_comp:
    blackjack = True

# Betting by user

  print(f"Cash:   {amount}")
  bet = int(input("Enter your bet:   "))
  cond = amount - bet
  if cond < 0:
    print("You don't have enough money to play")
    end = True
  else:
    blackjack_cash = bet / 2
    print("\n")

    # Insurance bet by user

    inbet = insurance(comp, cond)

    # Choosing between hit and double bet

    if not blackjack:

      print(f"\nYour cards: {user}     Total: {cards_sum(user)}\n")
      print(f"Dealer's first card: {comp[0]}\n")
      hit_bet = input(
          "Do you want to hit or double you bet?\nHit/Double:   ").lower()
      if hit_bet == "double":
        cond = cond - (bet / 2)
        if cond < 0:
          print("\nYou don't have enough money to play double bet\n")
        else:
          bet = bet * 2
          stand = True
          user.append(random.choice(cards))
          if cards_sum(user) > 21 and 11 in user:
            user[user.index(11)] = 1
        print("\n")

      # Hit starting by user
      while not stand:
        print(f"\nYour cards: {user}     Total: {cards_sum(user)}\n")
        print(f"Dealer's first card: {comp[0]}\n")
        hit_stand = input("Press 'y' to hit or 'n' to stand:   ").lower()
        print("\n")
        if hit_stand == "y":
          user.append(random.choice(cards))
          if cards_sum(user) > 21 and 11 in user:
            user[user.index(11)] = 1

          if cards_sum(user) > 21 or cards_sum(user) == 21:
            stand = True
        elif hit_stand == "n":
          stand = True

        # Stand starts
      if cards_sum(user) < 22:
        while cards_sum(comp) < 17:
          comp.append(random.choice(cards))
          if cards_sum(comp) > 21 and 11 in comp:
            comp[comp.index(11)] = 1
          if cards_sum(comp) > 21:
            win = True

      user_total = cards_sum(user)
      comp_total = cards_sum(comp)

      # Calculating winner

      if user_total < 22 and comp_total < 22:
        if user_total > comp_total:
          win = True
        elif user_total < comp_total:
          win = False
        elif user_total == comp_total:
          push = True
      elif user_total > 21:
        win = False

      print(f"\n Your cards: {user}    Total: {user_total}\n")
      print(f"Dealer's cards: {comp}   Total: {comp_total}")

      if blackjack_user:
        print("You have a blackjack!\n")
      if blackjack_comp:
        print("Dealer has a blackjack!\n")

      if not push:
        if win and not push:
          print("\nYou win!!")
          win_count += 1
        else:
          print("\nYou lost!!")
          bet = bet * -1
      else:
        print("\nIt's a draw!!")
        bet = 0

    amount = amount + bet
    amount += inbet
    if blackjack_user:
      amount += blackjack_cash
    if amount > high:
      high = amount

    if amount == 0:
      end = True
      clear()
    else:

      choice = input(
          "\n\nDo you want to continue or cash out?\nC to continue, E to cash out:    "
      ).lower()
      clear()
      if choice == "c":
        end = False
      elif choice == "e":
        end = True

print("GoodBye\n")
print(
    f"Cash won:       {amount-1000}\nHands won:      {win_count}\nHighest bank:   {high}"
)
