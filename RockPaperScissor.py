import random


# P for paper, R for Rock, S for scissor and Q for quit

wins = loses = ties = 0
moves = {"p":"Paper", "r":"Rock", "s":"Scissor"}
player_move = "dlfj"


def get_player_move():

    player_move = input("Choose your move (R)ock, (P)aper, (S)cissor and (Q)uit! : ").lower()
    if player_move not in ["r","p","s","q"]:
        print("Invalid Choice! Please Pick again!")
        print("\n")
        return get_player_move()
    return player_move


def get_comp_move():

    comp_move = random.choice(["r", "p", "s"])
    return comp_move


def result(player_move, comp_move):
    # R>S, P>R AND S>P

    global wins, loses, ties
    if comp_move == player_move:
        print("It's a tie!")
        ties += 1
    
    elif (player_move=="p" and comp_move=="r") or \
         (player_move=="r" and comp_move=="s") or \
         (player_move=="s" and comp_move=="p"):
        print("You win!")
        wins += 1

    else:
        print("You Lost!")
        loses += 1

def display_moves(player_move, comp_move):
    print("\n")
    print(f"{moves[player_move]} versus ...")
    print(moves[comp_move])



print("\n")
print("ROCKS, PAPERS AND SCISSORS")
print("\n"*2)

while player_move != "q":
    print(f"You have {wins} wins, {ties} ties and {loses} losses!")
    print("\n")

    player_move = get_player_move()
    if player_move == "q":
        print("\n")
        print(f"Your final scores are {wins} wins, {ties} ties and {loses} losses!")
        break
    comp_move = get_comp_move()

    display_moves(player_move, comp_move)
    result(player_move, comp_move)
    print("\n")