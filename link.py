#! /usr/bin/env python

class Link:
	def __init__(self, param_endA, param_endB):
		self.sideA = param_endA
		self.sideB = param_endB
		self.message = []

	def __del__(self):
		self.message = []
		self.sideA = None
		self.sideB = None
		
	def unlink(self,param_id):
		pass
		
	
