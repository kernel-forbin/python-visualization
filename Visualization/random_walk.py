#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  3 21:00:34 2022

@author: dfost
"""
from random import choice

class RandomWalk:
    """a class to generate random walks"""
    
    def __init__(self, num_points=5000):
        self.num_points = num_points
        
        #all walks start at (0,0).
        self.x_values = [0]
        self.y_values = [0]
        
    def fill_walk(self):
        """calculate all the points of the walk"""
            
        #keep taking steps until the walk reaches the desired length.
        while len(self.x_values) < self.num_points:
                
            #decide which direstion to go and how far to go in that direction.
            x_direction = choice([1, -1])
            x_distance = choice([0, 1, 2, 3, 4])
            x_step = x_direction * x_distance
                
            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance
                
            #reject moves that go nowhere
            if x_step == 0 and y_step == 0:
                    continue
                
            #calculate the new position
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step
                
            self.x_values.append(x)
            self.y_values.append(y)
                