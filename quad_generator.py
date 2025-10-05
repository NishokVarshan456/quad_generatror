#author -> Nishok
#quad generator that generate points inside
from random import random
import csv

def tri_area(a1, a2, a3):
    return abs((a1[0]*(a2[1]-a3[1]) + a2[0]*(a3[1]-a1[1]) + a3[0]*(a1[1]-a2[1])) / 2.0)    

def point_inside_Tri(p1,p2,p3,p4):
    A=tri_area(p1,p2,p3)
    A1=tri_area(p1,p2,p4)
    A2=tri_area(p1,p3,p4)
    A3=tri_area(p2,p3,p4)
    if (A==A1+A2+A3):
        return True
    else:
        return False
    
 
def Tri_gen(p1, p2, p3):
    while True:
 
        a = random()
        b = random()
        g = random()
 
        tot = a + b + g
 
        a = a / tot
        b = b / tot
        g = g / tot
 
        new_point = []
        new_point = [
            a * p1[0] + b * p2[0] + g * p3[0],
            a * p1[1] + b * p2[1] + g * p3[1],
            a * p1[2] + b * p2[2] + g * p3[2]
        ]
 
        yield new_point
 
def quad_gen(p1, p2, p3, p4):
    if point_inside_Tri(p1, p2, p3, p4):
        tri1 = Tri_gen(p1, p2, p4)
        tri2 = Tri_gen(p2, p3, p4)
        
    elif point_inside_Tri(p2, p3, p4, p1):
        tri1 = Tri_gen(p2, p3, p1)
        tri2 = Tri_gen(p3, p4, p1)
        
    elif point_inside_Tri(p3, p4, p1, p2):
        tri1 = Tri_gen(p3, p4, p2)
        tri2 = Tri_gen(p4, p1, p2)
        
    elif point_inside_Tri(p4, p1, p2, p3):
        tri1 = Tri_gen(p4, p1, p3)
        tri2 = Tri_gen(p1, p2, p3)
        
    else:
        tri1 = Tri_gen(p1, p2, p3)
        tri2 = Tri_gen(p1, p3, p4)
            
    while True:
        yield next(tri1)
        yield next(tri2)
 
result=quad_gen([4,5,0], [7,6,0], [4,3,0], [1,2,0])
with open('quad_gen_file.csv','w') as f:
    for i in range(50000):
        x,y,z=next(result)
        f.write(str(x)+", "+str(y)+", "+str(z)+"\n")

