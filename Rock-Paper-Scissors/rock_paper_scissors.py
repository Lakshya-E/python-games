import random

print("Lets Play Rock, Paper and Scissors")
try:
    T = int(input("How many rounds you want to play?\n>> "))
except ValueError:
    print("Run Again")
else:
    choices = ["Rock", "Scissors", "Paper"]
    gifs = ['🪨', '✂️', '📄']

    sum_us, sum_ai = 0, 0

    for i in range(0, T):
        while True:
            your_choice = int(input("Enter 0 for rock, 1 for scissors, 2 for paper\n>> "))
            if your_choice == 0 or your_choice == 1 or your_choice == 2:
                break
            print("Please Enter correct option")

        ai_choice = random.randint(0, 2)
        print(f'''Your Choice: {choices[your_choice]}
    
                    {gifs[your_choice]}
    
    ''')
        print(f'''Computer's Choice: {choices[ai_choice]}
    
                    {gifs[ai_choice]}
    
    ''')

        if your_choice == 0 and ai_choice == 1:
            sum_us += 1
            print("You Win!!")
        elif your_choice == 0 and ai_choice == 2:
            sum_ai += 1
            print("You Lose")
        elif your_choice == 1 and ai_choice == 0:
            sum_ai += 1
            print("You Lose")
        elif your_choice == 1 and ai_choice == 2:
            sum_us += 1
            print("You Win!")
        elif your_choice == 2 and ai_choice == 0:
            sum_us += 1
            print("You Win!")
        elif your_choice == 2 and ai_choice == 1:
            sum_ai += 1
            print("You Lose")
        else:
            print("Its a Draw!!")
    if sum_us > sum_ai:
        msg = 'You are the Winner🔥!!!'
    elif sum_us == sum_ai:
        msg = ' Its a Draw😂!'
    else:
        msg = 'You lost the game😭'
    print(f'''
    
                    Total Score
    You - {sum_us}                          Computer - {sum_ai}
                  {msg}''')
