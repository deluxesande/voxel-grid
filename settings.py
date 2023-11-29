from numba import njit
import numpy as np
import glm
import math

# Resolution
WIN_RES = glm.vec2(800, 450)
# WIN_RES = glm.vec2(1600, 900)

# Colors
BG_COLOR = glm.vec3(0.1, 0.16, 0.25)


# Camera settings
FOV = 50  # deg
NEAR = 0.1
FAR = 100
SPEED = 0.01
SENSITIVITY = 0.05
