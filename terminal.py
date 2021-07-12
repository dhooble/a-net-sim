#!/usr/bin/env python

"""File describing the behavior of a terminal, mobile node"""

from node import Node


class Terminal(Node):

    def __init__(self, param_id, param_x=0, param_y=0):
        super().__init__(param_id, param_x, param_y)

