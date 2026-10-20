import random

class Die:
    ## models a single 6 sided die
    def roll(self):
        return random.randint(1, 6)

class Player:
    ## makes a single player and tracks their total score
    def __init__(self, name):
        self.name = name
        self.score = 0

    def add_score(self, points):
        self.score += points

class Game:
    ## make the game environment and conditions and turn logic
    def __init__(self):
        self.players = [Player("Player 1"), Player("Player 2")]
        self.die = Die()
        self.current_player_idx = 0

    def play(self):
        print("Welcome to Pig")
        
        ## the game continues until a player's score is >= 100
        while self.players[0].score < 100 and self.players[1].score < 100:
            current_player = self.players[self.current_player_idx]
            print(f"\n{current_player.name}'s Turn ")
            
            turn_total = 0
            turn_active = True
            
            while turn_active:
                ## outputs the current totals before asking for a decision
                print(f"Turn Total: {turn_total} | Overall Score: {current_player.score}")
                decision = input("Enter 'r' to roll or 'h' to hold: ").lower()
                
                if decision == 'r':
                    roll_value = self.die.roll()
                    print(f"You rolled a {roll_value}!")
                    
                    if roll_value == 1:
                        print("Piged out! You score 0 for this turn.")
                        turn_total = 0
                        turn_active = False
                    else:
                        turn_total += roll_value
                
                elif decision == 'h':
                    current_player.add_score(turn_total)
                    print(f"{current_player.name} holds. Added {turn_total} to total score.")
                    print(f"New Overall Score: {current_player.score}")
                    turn_active = False
                
                else:
                    print("Invalid input. Please enter 'r' or 'h'.")
            
            ## checks for win condition immediately after a player holds
            if current_player.score >= 100:
                print(f"\n {current_player.name} wins with a score of {current_player.score}! ")
                break
                
            ## switchs to the other player
            self.current_player_idx = 1 if self.current_player_idx == 0 else 0
    def reset(self):
        ## resets the game memory for a new game
        for player in self.players:
            player.score = 0
        self.current_player_idx = 0
        print("\n New game has begun")

if __name__ == "__main__":
    ## sets the random seed to 0 at the beginning of the code for testability
    random.seed(0)
    
    ## starts a single game instance
    pig_game = Game()
    pig_game.play()
if __name__ == "__main__":
    ## sets the random seed to 0 at the beginning of the code for testability
    random.seed(0)
    
    ## starts a single game instance
    pig_game = Game()

while True:
    pig_game.play() 

    replay = input("\n Do you want play again?  (y/n)": ).lower()
    if replay == 'y':
        pig_game.reset()
    else:
        print("Thanks for playing")
        break
