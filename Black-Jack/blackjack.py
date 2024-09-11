import random
import pyautogui
import art

CARDS = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def make_bet(balance):
    balance_check = [1, 2, 5, 25, 50, 100, 200,
                     500, 1000, 2000, 5000, 10000]
    bet_sum = 0
    available_bets = []

    while True:
        if balance == 0:
            print(f"""
********************************
    Your total bet is ${bet_sum} 
********************************\n""")
            break
        print(f"Your Balance: ${balance}\n"
              f"Total Bet ${bet_sum}\n\n"
              "Bets you can make: ")

        for bet in balance_check:
            if bet <= balance:
                available_bets.append(bet)
                print(f"${bet}", end=", ")
        print("\n")

        total_bet = input("""Press 'b' to confirm the bet or
Enter bet value: $""")

        if total_bet.isdigit():
            total_bet = int(total_bet)
            if total_bet < 1:
                print("Enter a value more than 0")
            elif total_bet not in available_bets:
                print("Enter a value from the available bets")
            else:
                bet_sum += total_bet
                balance -= total_bet
        elif total_bet == 'b':
            if bet_sum < 1:
                print("Bet value should be more than 0")
            else:
                print(f"""
********************************
    Your total bet is ${bet_sum} 
********************************\n""")
                break
        else:
            print("Enter a number!")
        print()

    return bet_sum, balance


def clear_for_ace(cards):
    ind = cards.index(11)
    cards[ind] = 1
    total_sum = sum(cards)
    return cards, total_sum


def check_dealer_sum(dealer_cards, total_dealer_sum, total_user_sum):
    while total_user_sum > total_dealer_sum:
        if 17 <= total_dealer_sum <= 21:
            return dealer_cards, total_dealer_sum

        dealer_cards.append(random.choice(CARDS))
        total_dealer_sum = sum(dealer_cards)

        if total_dealer_sum > 21:
            if 11 in dealer_cards:
                dealer_cards, total_dealer_sum = clear_for_ace(dealer_cards)

    return dealer_cards, total_dealer_sum


def game(user_cards, dealer_cards, bet, balance, highest_balance):
    total_user_sum = sum(user_cards)
    total_dealer_sum = sum(dealer_cards)

    if total_user_sum == 21:
        dealer_cards, total_dealer_sum = check_dealer_sum(dealer_cards, total_dealer_sum, total_user_sum)
        if total_dealer_sum == total_user_sum:
            print(f"""
********************************
It's a Draw
His cards are {dealer_cards} and sum is {total_dealer_sum}
Your cards are {user_cards} and sum is {total_user_sum}
********************************\n""")

        elif total_dealer_sum < total_user_sum:
            print(f"""
********************************
You Won!!!
His cards are {dealer_cards} and sum is {total_dealer_sum}
Your cards are {user_cards} and sum is {total_user_sum}
********************************\n""")
            bet *= 3

        restart_game(bet, balance, highest_balance)
        return

    elif total_user_sum > 21:
        if 11 in user_cards:
            user_cards, total_user_sum = clear_for_ace(user_cards)
        else:
            print(f"""
********************************
Dealer Won
His cards are {dealer_cards} and sum is {total_dealer_sum}
Your cards are {user_cards} and sum is {total_user_sum}
********************************\n""")
            bet = 0
            restart_game(bet, balance, highest_balance)
            return

    print(f'''Your cards are {user_cards} and your sum is {total_user_sum}
Dealer cards are [{dealer_cards[0]},'hidden']\n''')

    choice = input("""If you want to add cards, press 'a'
If you want to fold, press 'f'\n>>>""")

    if choice == 'a':
        user_cards.append(random.choice(CARDS))
        game(user_cards, dealer_cards, bet, balance, highest_balance)

    elif choice == 'f':
        dealer_cards, total_dealer_sum = check_dealer_sum(dealer_cards, total_dealer_sum, total_user_sum)

        if total_dealer_sum > total_user_sum:
            if total_dealer_sum <= 21:
                print(f"""
********************************9
Dealer Won
His cards are {dealer_cards} and sum is {total_dealer_sum}
Your cards are {user_cards} and sum is {total_user_sum}
********************************\n""")
                bet = 0

            elif total_dealer_sum > 21:
                print(f"""
********************************
You Won!!!
His cards are {dealer_cards} and sum is {total_dealer_sum}
Your cards are {user_cards} and sum is {total_user_sum}
********************************\n""")
                bet *= 2

        elif total_dealer_sum == total_user_sum:
            print(f"""
********************************
It's a Draw
His cards are {dealer_cards} and sum is {total_dealer_sum}
Your cards are {user_cards} and sum is {total_user_sum}
********************************\n""")

        else:
            print(f"""
********************************
You Won!!!
His cards are {dealer_cards} and sum is {total_dealer_sum}
Your cards are {user_cards} and sum is {total_user_sum}
********************************\n""")
            bet *= 2

        restart_game(bet, balance, highest_balance)
        return
    else:
        print("Enter correct value\n")
        game(user_cards, dealer_cards, bet, balance, highest_balance)


def restart_game(bet, balance, highest_balance):
    balance += bet

    if balance > highest_balance:
        highest_balance = balance

    if balance == 0:
        print(f"\nYour Total Balance ${balance}\nHighest Amount you got ${highest_balance}\n")
        art.thanks()
        return

    print(f"Your total balance ${balance}\n"
          f"You won ${bet}\n")

    choice = input("""Press 'r' make another bet
Press 's' to start a new game
Press 'q' to quit\n>>>""")

    if choice == 'r':
        user_cards = [random.choice(CARDS), random.choice(CARDS)]
        dealer_cards = [random.choice(CARDS)]
        pyautogui.hotkey('ctrl', ',')

        art.welcome()
        bet, balance = make_bet(balance)
        game(user_cards, dealer_cards, bet, balance, highest_balance)

    elif choice == 's':
        pyautogui.hotkey('ctrl', ',')
        main('s')

    elif choice != 'q':
        print("Press correct option")
        restart_game(bet, balance, highest_balance)

    else:
        print(f"\nYour Total Balance ${balance}\nHighest Amount you got ${highest_balance}\n")
        art.thanks()
        return


def main(user_input):
    balance = 800
    highest_balance = -1
    user_cards = [random.choice(CARDS), random.choice(CARDS)]
    dealer_cards = [random.choice(CARDS)]

    if user_input == 's':
        art.welcome()

        bet, balance = make_bet(balance)
        game(user_cards, dealer_cards, bet, balance, highest_balance)
    elif user_input == 'q':
        art.thanks()
    else:
        print("Enter correct value")
        user_input = input("Press 's' or type 'q' to start ")
        main(user_input)


USER_INPUT = input("Press 's' to start or type 'q' to quit: ")
main(USER_INPUT)
