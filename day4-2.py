# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 10:43:45 2020

@author: user
"""


from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x,y,z=mc.player.getTilePos()
import random
x,y,z=mc.player.getTilePos()
for i in range(20):
    r = random.randrange(1,5)
    
    if r == 1:
        mc.setBlocks(x,y,z,x+4,y,z,46)
        x = x+4
    elif r == 2:
        mc.setBlocks(x,y,z,x-4,y,z,46)
        x = x-4
    elif r == 3:
        mc.setBlocks(x,y,z,x,y,z+4,46)
        z = z+4
    elif r == 3:
        mc.setBlocks(x,y,z,x,y,z-4,46)
        z = z-4
        