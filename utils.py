import math
import numpy as np
import pygame
import ship

# Rotate a 2D vector by a certain angle
def rotate(vector, angle):
    #b = np.multiply(vector,angle)
    b = pygame.transform.rotate(DISPLAYSURF, angle)

	# Action required!
    return b

# Map a value fr om one range to another
def map(n, start1, stop1, start2, stop2):
    newval = (n - start1) / (stop1 - start1) * (stop2 - start2) + start2;

    if newval > stop2:
        return stop2
    elif newval < start2:
        return start2
    else:
        return newval