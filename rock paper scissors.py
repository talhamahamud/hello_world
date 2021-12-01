import random
def play():
    user=input("pls input 'r' for Rock, 'p' for paper and 's' for scissor: ")
    computer_choice=random.choice(['r', 'p', 's'])
    if user==computer_choice:
        return 'Tie'
    if is_win(user, computer_choice):
        return 'you win'
    return 'you lose'
def is_win(player, opponent):
    if (player=='r' and opponent=='s') or (player=='p' and opponent=='r') or (player=='s' and opponent=='p'):
        return True
print(play())