#!/usr/bin/env python

"""test file for Ad-Hoc network simulation"""

import tkinter
import grid
import pynput
import node,tower,terminal

HEIGHT = 720
WIDTH = 1280

# init tk
root = tkinter.Tk()

# create canvas
myCanvas = tkinter.Canvas(root, bg="white", height=HEIGHT, width=WIDTH)

loc_grid = grid.Grid(myCanvas,WIDTH,HEIGHT)
myCanvas.pack()
n1 = terminal.Terminal(1,600,600)
t1 = tower.Tower(1,700,700)
loc_grid.addTerminal(n1)
loc_grid.addTower(t1)
loc_grid.drawTerminals()
loc_grid.drawTowers()

# add to window and show
#myCanvas.pack()
root.mainloop()
