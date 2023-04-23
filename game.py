from tkinter import *
import random

GRID_SIZE = 20
SQUARE_SIZE = 20
MINES_NUM = 40
mines = set(random.sample(range(1, GRID_SIZE**2+1), MINES_NUM))
clicked = set()

def check_mines(neighbors):
    return len(mines.intersection(neighbors))

def generate_neighbors(square):
    if square == 1:
        data = {GRID_SIZE + 1, 2, GRID_SIZE + 2}
    elif square == GRID_SIZE ** 2:
        data = {square - GRID_SIZE, square - 1, square - GRID_SIZE - 1}
    elif square == GRID_SIZE:
        data = {GRID_SIZE - 1, GRID_SIZE * 2, GRID_SIZE * 2 - 1}
    elif square == GRID_SIZE ** 2 - GRID_SIZE + 1:
        data = {square + 1, square - GRID_SIZE, square - GRID_SIZE + 1}
    elif square < GRID_SIZE:
        data = {square + 1, square - 1, square + GRID_SIZE,
                square + GRID_SIZE - 1, square + GRID_SIZE + 1}
    elif square > GRID_SIZE ** 2 - GRID_SIZE:
        data = {square + 1, square - 1, square - GRID_SIZE,
                square - GRID_SIZE - 1, square - GRID_SIZE + 1}
    elif square % GRID_SIZE == 0:
        data = {square + GRID_SIZE, square - GRID_SIZE, square - 1,
                square + GRID_SIZE - 1, square - GRID_SIZE - 1}
    elif square % GRID_SIZE == 1:
        data = {square + GRID_SIZE, square - GRID_SIZE, square + 1,
                square + GRID_SIZE + 1, square - GRID_SIZE + 1}
    else:
        data = {square - 1, square + 1, square - GRID_SIZE, square + GRID_SIZE,
                square - GRID_SIZE - 1, square - GRID_SIZE + 1,
                square + GRID_SIZE + 1, square + GRID_SIZE - 1}
    return data

def clearance(ids):
    clicked.add(ids)
    ids_neigh = generate_neighbors(ids)
    around = check_mines(ids_neigh)
    c.itemconfig(ids, fill="green")

    if around == 0:
        neigh_list = list(ids_neigh)
        while len(neigh_list) > 0:
            item = neigh_list.pop()
            c.itemconfig(item, fill="green")
            item_neigh = generate_neighbors(item)
            item_around = check_mines(item_neigh)
            if item_around > 0:
                if item not in clicked:
                    x1, y1, x2, y2 = c.coords(item)
                    c.create_text(x1 + SQUARE_SIZE / 2,
                                  y1 + SQUARE_SIZE / 2,
                                  text=str(item_around),
                                  font="Arial {}".format(int(SQUARE_SIZE / 2)),
                                  fill='yellow')
            else:
                neigh_list.extend(set(item_neigh).difference(clicked))
                c.itemconfig(item, fill="green")
                if item not in clicked:
                    clearance(item)

def check_game():
    if clicked == mines:
        c.create_text(GRID_SIZE * SQUARE_SIZE / 2, GRID_SIZE * SQUARE_SIZE / 2,
                      text="You Win!", font="Arial {}".format(int(SQUARE_SIZE * 2)),
                      fill='yellow')
    else:
        for mine in mines:
            if mine in clicked:
                continue
           
