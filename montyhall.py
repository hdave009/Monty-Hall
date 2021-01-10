import random


def monty_hall(choice, switch):
    prizes = ['g', 'g', 'c']
    prizes_randomized = random.sample(prizes, 3)
    combos = [(i+1, p) for i, p in enumerate(prizes_randomized)]

    doors = ["Door 1", "Door 2", "Door 3"]
    # print(doors)
    door_selected = choice
    #print("You have chosen Door", door_selected)

    unopened = []
    for door in combos:
        door_num = door[0]
        if door_num != door_selected:
            unopened.append(door)

    mhopened = list(filter(lambda d: d[1] == 'g', unopened))[0][0]

    #print("Monty Hall has revealed a door with a goat:")
    doorsUpdated = [door if door != "Door " +
                    str(mhopened) else 'g' for door in doors]
    closed = [int(s[5])
              for s in list(filter(lambda e: e != 'g', doorsUpdated))]
    # print(doorsUpdated)

    if(switch == True):
        newDoor = int(
            list(filter(lambda e: e != door_selected, closed))[0])
        if(combos[newDoor-1][1] == 'c'):
            return True
        else:
            return False
    else:
        if(combos[door_selected-1][1] == 'c'):
            return True
        else:
            return False


def test_monty_hall(rounds, switch):
    w = 0
    l = 0
    for i in range(rounds):
        outcome = monty_hall(random.randint(1, 3), switch)
        if(outcome == True):
            w += 1
        else:
            l += 1
    outcomes = [("W", w), ("L", l)]
    return outcomes


print(test_monty_hall(9, True))
