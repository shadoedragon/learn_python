from math import *

# CHAPTER 1

def greet(name):
    print("Hello %s!" % name)

def square(x):
    return x * x

# CHAPTER 2

# addition of 2 2-dim vectors
def vector_add(v1, v2):
    return (v1[0]+v2[0], v1[1]+v2[1])

def vector_add_all(*vectors):
    return (sum([v[0] for v in vectors]), sum([v[1] for v in vectors]))

# minus of 2 2-dim vectors
def vector_minus(v1, v2):
    return (v1[0]-v2[0], v1[1]-v2[1])

def vector_length(v):
    return sqrt(square(v[0])+square(v[1]))

# distance of 2 2-dim vector
def distance(v1, v2):
    return vector_length(vector_minus(v1,v2))

# perimeter of multiple vectors
def perimeter(vectors):
    distances = [distance(vectors[i], vectors[(i+1)%len(vectors)])
                for i in range(0,len(vectors))]
    return sum(distances)

# 2-dim vectors times a number
def vector_scale(scalar, v):
    return (v[0]*scalar, v[1]*scalar)

# translate function, get one shifting vector and vector list, return the shifted vector list
def translate(translation, vectors):
    return [vector_add(translation, v) for v in vectors]

def to_cartesian(polar_vector):
    length, angle = polar_vector[0], polar_vector[1]
    return (length*cos(angle), length*sin(angle))

def to_polar(vector):
    x, y = vector[0], vector[1]
    angle = atan2(y, x)
    return (vector_length(vector), angle)

def rotate(angle, vectors):
    rotation_angle = angle * pi / 180
    vectors_polar = [to_polar(v) for v in vectors]
    vectors_rotated_polar = [(l, angle + rotation_angle) for l, angle in vectors_polar]
    vectors_rotated = [to_cartesian(p) for p in vectors_rotated_polar]
    return vectors_rotated

# calculate regular polygon, return one vector with Cartesian coordination value
def regular_polygon(length, n):
    return [to_cartesian((length, 2*pi*k/n)) for k in range(0,n)]