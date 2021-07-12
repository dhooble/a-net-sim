#!/usr/bin/env python

"""File describing the behavior of the grid"""

TERMINAL_RADIUS_DRAW = 10
TOWER_SIDE_DRAW = 10

class Grid:
	def __init__(self, param_canvas = None, param_sizeX=5, param_sizeY=5, param_grid_spacing = 20):
		self.sizeX = param_sizeX
		self.sizeY = param_sizeY
		self.grid_spacing = param_grid_spacing
		self.nbCasesX = int(self.sizeX/self.grid_spacing)
		self.nbCasesY = int(self.sizeY/self.grid_spacing)
		self.canvas = param_canvas
		self.list_terminal = {}
		self.list_tower = {}
		

	def drawGrid():
		pass

	
	def addTerminal(self, terminal):
		""" Adding a terminal to the list of existing terminals on the grid """
		if not(terminal.getId() in self.list_terminal):
			self.list_terminal[terminal.getId()] = terminal

	def removeTerminal(self, terminal):
		""" removing a terminal from the list of existing terminals on the grid """
		if terminal.getId() in self.list_terminal:
			del self.list_terminal[terminal.getId()]

	def addTower(self, tower):
		""" Adding a tower to the list of existing towers on the grid """
		if not(tower.getId() in self.list_tower):
			self.list_tower[tower.getId()] = tower

	def removeTower(self, tower):
		""" removing a tower from the list of existing towers on the grid """
		if tower.getId() in self.list_tower:
			self.list_tower[tower.getId()] = tower
	
	def drawTerminals(self):
		""" drawing every known terminal as circles """
		for terminal in self.list_terminal.values():
			print('teminal : x : {} ; y : {}'.format(terminal.getX(), terminal.getY()))
			self.canvas.create_oval(terminal.getX()-TERMINAL_RADIUS_DRAW,terminal.getY()-TERMINAL_RADIUS_DRAW,terminal.getX()+TERMINAL_RADIUS_DRAW,terminal.getY()+TERMINAL_RADIUS_DRAW, fill="black")
	
	def drawTowers(self):
		""" drawing every known towers as squares """
		for tower in self.list_tower.values():
			self.canvas.create_rectangle(tower.getX()-TOWER_SIDE_DRAW,tower.getY()-TOWER_SIDE_DRAW,tower.getX()+TOWER_SIDE_DRAW,tower.getY()+TOWER_SIDE_DRAW, fill="green")