import copy
import time
import curses
import random
import os
import sys
k_players = []



lab = [ list("____________________"),
        list("|             #    |"),
        list("|    ####     #    |"),
        list("|     #       #    |"),
        list("| #   #      ####  |"),
        list("| #   ####     #   |"),
        list("| # #          #   |"),
        list("|___#####___________") ]

lab = [ list("   "),
        list("   "),
        list("   ")]

max_x = len(lab) - 1
max_y = len(lab[0]) - 1

x = random.randint(0, max_x)
y = random.randint(0, max_y)


players = [['?', 1, 1], ["$", 7, 19]]
me = ['!', 3, 3]


#ya = lab[x],[y]
#print(ya)
while True:
    copylab = copy.deepcopy(lab)
    for n in range(len(players)):

        player = players[n]
        new_x = x + random.randint(0, 2) - 1
        new_y = y + random.randint(0, 2) - 1

        while new_x < 0 or new_x > max_x:
            new_x = x + random.randint(0, 2) - 1

        while new_y < 0 or new_y > max_y:
            new_y = y + random.randint(0, 2) - 1

#        if not ((copylab[new_x][new_y] == '#') or (copylab[new_x][new_y] == '|') or (copylab[new_x][new_y] == '_') or (copylab[new_x][new_y] == player[0]) ):
        if copylab[new_x][new_y] == ' ':
            x = new_x
            y = new_y

            players[n] = [player[0], x,y]
            print(x, y)

        copylab[x][y] = player[0]

        if player[1] == 2 and player[2] == 2:
            for i in range(len(players)):
                if not(i == n):
                    skin, x, y = players[i]
                    copylab[x][y] ='Ⴕ'

            for q in copylab:
                s = ''.join(q)
                print(s)
            sys.exit(0)

    for q in copylab:
       s = ''.join(q)
       print(s)

    time.sleep(1)

    os.system('clear')

