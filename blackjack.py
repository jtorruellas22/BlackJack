import p1_random as p1
rng = p1.P1Random()
# Import and declared number randomizer
player_wins = 0
dealer_wins = 0
player_hand = 0
dealer_hand = 0
game_ties = 0
game_num = 0
game = 'new'
card_number = 0
player_choice = 0
card_name = ' '
hand_tracker = f'Your hand is: '
menu = f'1. Get another card\n'\
       f'2. Hold hand\n'\
       f'3. Print statistics\n'\
       f'4. Exit \n'\
       f'Choose an option: '
# All variable being used in this program
while player_hand <= 21:
    if game != 'same':
        card_number = rng.next_int(13) + 1
        if card_number == 1:
            card_name = "Your card is a ACE!"
            player_hand += 1
        elif card_number == 11:
            card_name = "Your card is a JACK!"
            player_hand += 10
        elif card_number == 12:
            card_name = "Your card is a QUEEN!"
            player_hand += 10
        elif card_number == 13:
            card_name = "Your card is a KING!"
            player_hand += 10
        else:
            card_name = f"Your card is a {card_number}!"
            player_hand += card_number
# Card generator assuming option 3 was not selected.
    if game == 'new':
        game_num += 1
        print('START GAME #', game_num, '\n')
        print(card_name)
        print(hand_tracker, player_hand, '\n')
        print(menu)
        player_choice = int(input())
        game = ' '
    # Print Statement assuming it's a new game.
    # Prints card name, card value, player hand, and menu.
    # Asks for player input.
    elif game == 'same':
        print(menu)
        player_choice = int(input())
    # Print Statement assuming player chose option 3.
    # Prints menu.
    # Asks for player input.
    elif player_hand > 21:
        print(card_name)
        print(hand_tracker, player_hand, '\n')
        print("You exceeded 21! You lose.\n")
        dealer_wins += 1
        player_hand = 0
        player_choice = 0
        game = 'new'
    # Print Statement assuming player hand exceeds 21.
    # Prints card name, card value, and player hand.
    # Starts new game.
    elif player_hand == 21:
        print(card_name)
        print(hand_tracker, player_hand, '\n')
        print("BLACKJACK! You win!\n")
        player_wins += 1
        player_hand = 0
        player_choice = 0
        game = 'new'
    # Print Statement assuming player hand equals 21.
    # Prints card name, card value, and player hand.
    # Starts new game.
    else:
        print(card_name)
        print(hand_tracker, player_hand, '\n')
        print(menu)
        player_choice = int(input())
    # Print Statement assuming it's the same game and player did not choose option 3.
    # Prints menu.
    # Asks for player input.
    if game != 'new':
        if player_choice < 1 or player_choice > 4:
            game = 'same'
            print("Invalid input!")
            print("Please enter an integer value between 1 and 4.\n")
        # Tests player choice for valid input.
        elif player_choice == 1:
            player_hand = player_hand
            game = ' '
        # Allows loop to restart causing a new card to be drawn.
        elif player_choice == 2:
            dealer_hand = rng.next_int(11) + 16
            print("Dealer's hand: ", dealer_hand)
            print("Your hand is: ", player_hand, '\n')
            if dealer_hand > 21:
                print("You win!\n")
                player_wins += 1
                player_hand = 0
                game = 'new'
            elif player_hand == dealer_hand:
                print("It's a tie! No one wins!\n")
                game_ties += 1
                player_hand = 0
                game = 'new'
            elif player_hand > dealer_hand:
                print("You win!\n")
                player_wins += 1
                player_hand = 0
                game = 'new'
            elif player_hand < dealer_hand:
                print("Dealer wins!\n")
                dealer_wins += 1
                player_hand = 0
                game = 'new'
        # Creates Dealer hand and compares it to player hand.
        # Determines game winner or tie. Record game statistics.
        # Starts new game
        elif player_choice == 3:
            game = 'same'
            print("Number of Player wins: ", player_wins)
            print("Number of Dealer wins: ", dealer_wins)
            print("Number of tie games: ", game_ties)
            print("Total # of games played is: ", game_num - 1)
            print("Percentage of Player wins: ", round(player_wins / (game_num - 1) * 100, 1), '%\n')
        # Prints game statistics if player chose option 3
        elif player_choice == 4:
            break
        # Ends loop
