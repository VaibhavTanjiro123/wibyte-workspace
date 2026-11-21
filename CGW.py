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
pw=0
cw=0
gameover=False
movover=False
tablecards=[]
mp=0
while not gameover:
    movover=False
    if len(pc)<1 orlen(cc)<1:
        movover=True
        gameover=True
    while not movover:

        pcard=pc.pop(0)
        ccard=cc.pop(0)
        
        print("Player's card is",pcard)
        print("Computer's card is",ccard)
        tablecards.append(ccard)
        tablecards.append(ccard)
        if cards.index(pcard[1])>cards.index(ccard[1]):
            print('Player won this round!!!')
            input()
            pc.extend(tablecards)
            tablecards.clear()
            movover=True
            mp=mp+1
            pw=pw+1
        elif cards.index(pcard[1])<cards.index(ccard[1]):
            print('Computer won this round...:(')
            input()
            cc.extend(tablecards)
            tablecards.clear()
            movover=True
            mp=mp+1
            cw=cw+1
        else:
            print('War Begins')
            if len(pc)<4 orlen(cc)<4:
                movover=True
                gameover=True
            else:
                tablecards.extend(pc[0:3:1])
                tablecards.extend(cc[0:3:1])

                del pc[0:3:1]
                del cc[0:3:1]
        if mp >= 10:
            gameover=True

print('Player Cards:',len(pc),'Comp Cards:',len(cc),'Table Cards:'len(tablecards))
if pw>cw:
    
    print('PLAYER WON!!!')
elif cw>pw:
    print('COMPUTER WON!!!')
else:
    print('GAME TIED !!!')