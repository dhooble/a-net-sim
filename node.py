#!/usr/bin/env python

"""File describing the general behavior of a node"""

class Node:
	RANGE = 5
	def __init__(self, param_id, param_x=0, param_y=0):
		self.x = param_x
		self.y = param_y
		self.id = param_id
		self.link = []
		
	def __del__(self):
		for lk in self.link:
			lk.unlink()
		
		self.link.clear()
	
	def getId(self):
		return self.id
	
	def getX(self):
		return self.x

	def getY(self):
		return self.y

	def setX(self,param_x):
		self.x = param_x
	
	def setY(self,param_y):
		self.y = param_y
		
	def send_message(self):
		pass
		
	def recieve_message(self):
		pass
