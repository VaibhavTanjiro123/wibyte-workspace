cards=['2','3','4','5','6','7','8','9','X','J','Q', 'K', 'A']
suits=['C','D','S','H']
deck=[]
for kk in suits:
    for jj in cards:
        deck.append(kk+jj)
print(deck)