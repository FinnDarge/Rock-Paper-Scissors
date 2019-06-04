import random
"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

moves = ["rock", "paper", "scissors"]

"""The Player class is the parent class for all of the Players
in this game. Only plays rock"""


class Player:
    """setting the variables for storing the moves"""
    my_move = None
    their_move = None

    def move(self):
        return "rock"

    def learn(self, my_move, their_move):
        self.my_move = my_move
        self.their_move = their_move


"""Random Player that chooses randomly between the moves"""


class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)


"""Human Player with input that converts to lowercase and
 a while loop that runs until a valid weapon is chosen"""


class HumanPlayer(Player):
    def move(self):
        while True:
            choice = input("Choose Rock, Paper or Scissors or type Exit: ")
            if choice.lower() == "exit":
                exit(0)
            elif choice.lower() not in moves:
                print("Please Try A Valid Weapon!")
            else:
                return choice.lower()


"""ReflectPlayer copies the move from other player in the earlier round,
starts in round 2"""


class ReflectPlayer(Player):
    def move(self):
        if self.their_move is None:
            return random.choice(moves)
        else:
            return self.their_move


"""CyclePlayer that cycles through the weapons depending on which it
has chosen randomly in the first round"""


class CyclePlayer(Player):
    def move(self):
        if self.their_move is None:
            return random.choice(moves)
        if self.my_move == "rock":
            return "paper"
        if self.my_move == "paper":
            return "scissors"
        else:
            return "rock"


def beats(one, two):
    return ((one == "rock" and two == "scissors") or
            (one == "scissors" and two == "paper") or
            (one == "paper" and two == "rock"))


class Game:
    """Variables for the score of Player 1 or 2"""
    p1_score = 0
    p2_score = 0

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

        if beats(move1, move2) is True:
            self.p1_score += 1
            print("Player One Won!")
        elif beats(move2, move1) is True:
            self.p2_score += 1
            print("Player Two Won!")
        elif move1 == move2:
            print("It´s A Tie!")

    def play_game(self):
        print("Let The Game Begin!")

        while True:
            rounds = input("How Many Rounds Do You Want To Play?")
            if rounds.isnumeric():
                rounds = int(rounds)
                break
            print("Please Type In A Valid Number!")
        for round in range(rounds):
            print(f"Round {round}:")
            self.play_round()
        print("Game over!")
        if self.p1_score > self.p2_score:
            print("Player One is the Champ!")
        elif self.p2_score > self.p1_score:
            print("Player Two Chose The Best Weapons And Won The Battle!")
        else:
            print("It´s A Tie, You Should Restart The Game!")


if __name__ == "__main__":
    game = Game(HumanPlayer(), CyclePlayer())
    game.play_game()
