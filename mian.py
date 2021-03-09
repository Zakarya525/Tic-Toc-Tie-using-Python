from header import *
b = testing()
print('Player = X\tPlayer = 0')
b.board()
draw = 0
for i in range(0,5):
    b.input()
    draw += 1
if draw == 5 or draw == 4:
    print("NOT TIED")
    print("GAME DRAW")