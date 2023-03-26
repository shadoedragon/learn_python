from math_xiaoqi import vector_add
from vector_drawing import *

dino_vectors = [(6,4), (3,1), (1,2), (-1,5), (-2,5), (-3,4), (-4,4),
                (-5,3), (-5,2), (-2,2), (-5,0.5), (-4,0), (-2,1), (-1,0),
                (0,-3), (-1,-4), (1,-4), (2,-3), (1,-2), (3,-1), (5,1)]

# dino_vectors2 = [vector_add((1.5,2.5),v) for v in dino_vectors]

draw(
    Points(*dino_vectors, color=blue),
    Polygon(*dino_vectors, color=green)
    # Points(*dino_vectors2, color=purple),
    # Polygon(*dino_vectors2, color=red)
)