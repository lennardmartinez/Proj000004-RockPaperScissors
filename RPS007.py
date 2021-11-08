"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""
import random
names = ['Naruto', 'Goku', 'Ranma', 'Rowan']
names2 = ['Plex', 'Jacob', 'Coin', 'ARKK']
moves = ['rock', 'paper', 'scissors']
players = ['Player_Random', 'Player_Cycle', 'Player_Reflect']
"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    my_move = None
    their_move = None

    def __init__(self, name):
        self.name = name

    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass


class Player_Random(Player):
    def __init__(self, name):
        self.name = name

    def move(self):
        return random.choice(moves)


class Player_Human(Player):
    def __init__(self, name):
        self.name = name

    def move(self):
        while True:
            move = input("Rock, paper, scissors?").lower()
            if move in moves:
                return move


class Player_Reflect(Player):
    def __init__(self, name):
        self.name = name

    def learn(self, my_move, their_move):
        self.their_move = their_move

    def move(self):
        if self.their_move is None:
            return random.choice(moves)
        return self.their_move


class Player_Cycle(Player):
    def __init__(self, name):
        self.name = name

    def learn(self, my_move, their_move):
        self.my_move = my_move

    def move(self):
        if self.my_move is None:
            return random.choice(moves)
        elif self.my_move == 'rock':
            return 'paper'
        elif self.my_move == 'paper':
            return 'scissors'
        elif self.my_move == 'scissors':
            return 'rock'


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.p1score = 0
        self.p2score = 0

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)
        if move1 == move2:
            print("*** TIE ***")
        else:
            if beats(move1, move2):
                self.p1score += 1
            else:
                self.p2score += 1

    def keep_score(self):
        print(f"|| S ||")
        print(f"|| C ||")
        print(f"|| O ||Score: Player 1: {Player1.name}: {self.p1score}")
        print(f"|| R ||Score: Player 2: {Player2.name}: {self.p2score}")
        print(f"|| E ||")

    def startover(self):
        play = input("Would you like to play again? (y/n)")
        if play == 'y':
            print("Excellent! Restarting the game ...")
            game.play_game()
        elif play == 'n':
            print("Thanks for playing! See you next time.")
            exit()
        else:
            startover()

    def winner(self):
        if(self.p1score == self.p2score):
            print(f"It's a tie.  With a score of {self.p1score} to" +
                  " {self.p2score}")
        elif(self.p1score > self.p2score):
            print(f"{Player1.name} Wins! With a score of {self.p1score} to" +
                  " {self.p2score}")
        elif(self.p1score < self.p2score):
            print(f"{Player2.name} Wins! With a score of {self.p2score} to" +
                  " {self.p1score}")

    def play_game(self):
        print("Game start!")
        for round in range(8):
            print(f"Round {round}:")
            self.play_round()
            self.keep_score()
        self.winner()
        print("Game over!")
        self.startover()


if __name__ == '__main__':
    Player1Name = input("What is your name?")
    Player2Name = random.choice(names2)
    # PlayerStyle = random.choice(players)
    Player1 = Player_Human(Player1Name)
    Player2 = Player_Random(Player2Name)
    game = Game(Player1, Player2)
    game.play_game()
