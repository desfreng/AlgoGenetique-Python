#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  6 18:12:17 2018

@author: gabriel
"""
import os.path

import population
import noteur

n = noteur.Noteur(66)
p = population.Population(1000, 0.20, 0.1, population.Tirage.Proportionel, n)
generation = 0
p.initGeneration([1, 2, 3, 4, 5, 6, 7, 8, 9])


if os.path.isfile("pop"):
    os.remove("pop")
if os.path.isfile("stat"):
    os.remove("stat")

f = open("pop", "w")
f.write(str(p))
f.close()

s = open("stat", "w")

try:

    while not p:
        generation += 1
        print("Generation : {}".format(generation))
        p.selection()
        p.croisement()
        p.mutation()
        s.write(" ".join([str(p.statAlleles()[i]) for i in range(0, 9)]) +"\n")

finally:
    s.close()

print("Solution trouvée !")
print("\n".join([str(i) for i in p.solutions]))
