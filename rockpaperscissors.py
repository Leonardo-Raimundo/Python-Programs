import random

def play():
    user = input("What's you choice? 'r' for rock, 'p' for paper, 's' for scissors\n").lower()
    
    while user != 'r' and user != 'p' and user != 's':
        if user != 'r' and user != 'p' and user != 's':
            print("Wrong input. Use 'r', 'p', or 's'")
            
        user = input("What's you choice? 'r' for rock, 'p' for paper, 's' for scissors\n").lower()
        
    computer = random.choice(['r', 'p', 's'])
    
    if user == computer:
        return 'It\'s a tie'
    
    if is_win(user, computer):
        return 'You won!'
    
    return 'You lost!'
    
def is_win(player, opponent):
    #return true if the player wins
    #r > s, s > p, p > r
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True

print(play())