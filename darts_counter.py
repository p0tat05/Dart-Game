
def Get_Name(player_number):
    player_name = input(f"Enter {player_number} name: ")
    return player_name

def StartingScore():
    validating_score = True
    while(validating_score):
        try:
            score = int(input("Enter starting score: "))
            if score != 0:
                return score
        except ValueError:
            print("Try a valid number")

def Score(player_name, player_score, current_dart, dart_set):
    no_error = True
    while(no_error):
        try:
            score = int(input(f"Enter {player_name}'s score:{player_score} darts:{current_dart+1}/{dart_set}: "))
            return score
        except ValueError:
            print("Enter a valid score")

def SumDiff(initial_score, new_score):
    sum = initial_score - new_score
    return print(f"sum: {sum}")

def DartsThrown(plyr_name, plyr_score):
    dart_set = 3
    initial_score = plyr_score
    print(f"{plyr_name} Score: {plyr_score}")
    for dart in range(dart_set):
        if plyr_score < 0:
            plyr_score += Score(plyr_name, plyr_score, dart, dart_set)
        else:
            plyr_score -= Score(plyr_name, plyr_score, dart, dart_set)
             

        if plyr_score == 0:
            SumDiff(initial_score, plyr_score)
            return plyr_score

    SumDiff(initial_score, plyr_score)
    return plyr_score

def DartGame(player1, player1_score, player2, player2_score):
    while((player1_score !=0) or (player2_score != 0)):
        player1_score = DartsThrown(player1, player1_score)
        print(f"{player1} Score: {player1_score}")
        print()
        if player1_score == 0:
            print(f"{player1} won!")
            return 1

        player2_score = DartsThrown(player2, player2_score)
        print(f"{player2} Score: {player2_score}")
        print()
        if player2_score == 0:
            print(f"{player2} won!")
            return 2
        

def DisplayGame(player1, player2):

    initial_score = StartingScore()
    player1_score = initial_score
    player2_score = initial_score
    print()

    winner = DartGame(player1, player1_score, player2, player2_score)
    if winner == 1:
        player1_win = 1
        return player1_win
        

    elif winner == 2:
        player2_win = 2
        return player2_win
        

def AnotherMatch():
    another_game = input("Do you want to continue [y/n]: ")
    if another_game == 'n':
        return 0
    else:
        return 1

def main():
    player1_name = Get_Name(player_number = 1)
    player2_name = Get_Name(player_number = 2)
    print()

    player1_wins = 0
    player2_wins = 0

    points_game = True
    while (points_game):
        print(f"{player1_name}:{player1_wins} - {player2_wins}:{player2_name}")
        
        win = DisplayGame(player1_name, player2_name)

        if win == 1:
            player1_wins += 1
        
        else:
            player2_wins += 1
        print()

        more_matches = AnotherMatch()
        if more_matches == 0:
            return 0
        print("-------------------------------------------------------")
    

main()

