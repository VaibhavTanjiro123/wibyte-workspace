import random

cards=['2','3','4','5','6','7','8','9','X','J','Q', 'K', 'A']
suits=['C','D','S','H']
deck=[]
for kk in suits:
    for jj in cards:
        deck.append(kk+jj)
print(deck)

print('Shuffled Deck')
random.shuffle(deck)

print(deck)
toss = random.choice(deck)
if toss[0] == 'C' or toss[0] == 'D':
    print('player won the toss')
else:
    print('computer won the toss')

pc=deck[0:26:1]
cc=deck[26:52:1]

gameover=False
movover=False

while not gameover:
    while not movover:

        pcard=pc.pop(0)
        ccard=cc.pop(0)
        
        print("Player's card is",pcard)
        print("Computer's card is",ccard)
        