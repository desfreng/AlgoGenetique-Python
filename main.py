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
p = population.Population(5000, 0.25, 0.05, population.Tirage.Proportionel, n)
generation = 0
print("Génération n°{}".format(generation))

p.initGeneration([1, 2, 3, 4, 5, 6, 7, 8, 9])


if os.path.isfile("pop"):
    os.remove("pop")

with open("pop", 'w') as f:
    f.write(str(p))
    f.close()


while not p:
    generation += 1
    print("Génération n°{} : Selection".format(generation))
    p.selection()
    print("Génération n°{} : Croisement".format(generation))
    p.croisement()
    print("Génération n°{} : Mutation".format(generation))
    p.mutation()

print("Solution trouvée !")
print("\n".join([str(i) for i in p.solutions]))
