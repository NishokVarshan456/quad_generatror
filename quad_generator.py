#author -> Nishok
#quad generator that generate points inside
from random import random
import csv

def quad_generator(p1, p2, p3, p4):
    while True:
        if random()<0.5:
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

        else:
            a = random()
            b = random()
            g = random()

            tot = a + b + g

            a = a / tot
            b = b / tot
            g = g / tot

            new_point = []
            new_point = [
                a * p1[0] + b * p3[0] + g * p4[0],
                a * p1[1] + b * p3[1] + g * p4[1],
                a * p1[2] + b * p3[2] + g * p4[2]
            ]

        with open('quadcsvfile.csv', 'a', newline='\n') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(new_point)
        yield new_point

result=quad_generator([0,0,0,0],[1,0,0,0],[0,1,0,0],[0,0,0,1])
for i in range(5):

    print(next(result))
