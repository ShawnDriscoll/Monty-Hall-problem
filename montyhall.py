
import matplotlib.pyplot as plt
from game_tools.pydice import roll

games = 2500
wins1 = 0
wins2 = 0

# Use the Monte Carlo method for 2500 iterations

door_items = ['car', 'goat', 'goat']
successes_for_staying = []
successes_for_switching = []

for n in range(games):
    behind_door = ['', '', '']
    for i in door_items:
        not_placed_behind = True
        while not_placed_behind:
            r = roll('d3-1')
            if behind_door[r] == '':
                behind_door[r] = i
                not_placed_behind = False
    print(behind_door)

    winning_door = behind_door.index('car')
    chosen_door = roll('d3-1')

    show_goat = False
    while show_goat == False:
        shown_door = roll('d3-1')
        if shown_door != chosen_door and behind_door[shown_door] == 'goat':
            show_goat = True
    
    print(winning_door, chosen_door, shown_door)

    # stays
    if chosen_door == winning_door:
        wins1 += 1
    else:
        wins1 += 0
    successes_for_staying.append(wins1 / (n + 1))

    # switches
    switching = True
    while switching:
        new_door = roll('d3-1')
        if new_door != chosen_door and new_door != shown_door:
            switching = False
            if new_door == winning_door:
                wins2 += 1
            else:
                wins2 += 0
    successes_for_switching.append(wins2 / (n + 1))

plt.plot(list(range(games)), successes_for_switching, 'g', label='Switched')
plt.plot(list(range(games)), successes_for_staying, 'r', label='Stayed')
plt.legend()
plt.title('Monty Hall Winnings')
plt.xlabel('Games')
plt.ylabel('Success Rate')
plt.grid()
plt.show()
