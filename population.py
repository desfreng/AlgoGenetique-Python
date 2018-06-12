#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 28 22:33:11 2018

@author: gabriel
"""
from random import randint
from collections import Sequence
from copy import deepcopy
from enum import Enum
from math import floor

from individu import Individu
from abstract_noteur import AbstractNoteur


class Tirage(Enum):
    Uniforme = 1
    Proportionel = 2


class Population(Sequence):
    def __init__(self, size, fracSupr, fracMut, tirage, noteur):
        self._popSize = size
        self._fracSupr = fracSupr
        self._fracMut = fracMut
        self._sommesNotes = 0
        self._pop = list()
        self._sol = list()

        if not isinstance(noteur, AbstractNoteur):
            raise ValueError(AbstractNoteur)
        else:
            self._noteur = noteur

        if isinstance(tirage, Tirage):
            self._typeSelection = tirage
        else:
            raise ValueError(Tirage)

    def initGeneration(self, genes, rd=True):
        self._pop.clear()

        for a in range(self._popSize):
            self._pop.append(deepcopy(Individu(genes, rd)))
            self.noteIndi()

    def __str__(self):
        self._pop.sort()
        return "\n".join([str(i) for i in self._pop])

    def __repr__(self):
        return "\
Population : Noteur=\"{}\"\n\
             Taille Attendue={}, Taille Réelle={}\n\
             Part de Mutation={}%, Part de Supression={}%".format(
            self._noteur,
            self._popSize,
            len(self),
            int(self._fracMut * 100),
            int(self._fracSupr * 100),
        )

    def __bool__(self):
        return bool(self._sol)

    def __getitem__(self, index):
        return self._pop[index]

    def __len__(self):
        return len(self._pop)

    def noteIndi(self, index=None, individu=None):
        if index is not None:
            indi = self._pop[index]
        elif individu is not None:
            indi = individu
        else:
            indi = self._pop[-1]

        indi.note = self._noteur(indi)
        self._sommesNotes += indi.note

        if indi.note == 1:
            self._sol.append(deepcopy(indi))

    def _selectRandomIndividu(self):
        if self._typeSelection is Tirage.Uniforme:
            return self._pop[randint(0, len(self._pop) - 1)]

        else:
            sommeTemp = 0
            n = randint(1, self._sommesNotes - 1)

            for i in self._pop:
                sommeTemp += i.note

            #print("{} = {} ?".format(sommeTemp, self._sommesNotes))
            sommeTemp = 0

            for individu in self._pop:

                if individu.note != 0:

                    sommeTemp += individu.note

                    #print("{} dans {}:{}".format(n, sommeTemp - individu.note, sommeTemp))
                    if n in range(sommeTemp - individu.note, sommeTemp):
                        return individu

            raise Exception("Impossible de sélectionner un individu !")

    def mutation(self):

        for i in range(floor(self._popSize * self._fracMut)):
            indi = self._selectRandomIndividu()
            self._sommesNotes -= indi.note

            indi.swapAlleles(randint(0, 8), randint(0, 8))
            self.noteIndi(individu=indi)

    def croisement(self):
        while not len(self._pop) == self._popSize:
            pat1 = self._selectRandomIndividu().patrimoine
            pat2 = self._selectRandomIndividu().patrimoine

            crossPoint = randint(1, 7)
            pat = pat1[:crossPoint] + pat2[crossPoint:]

            self._pop.append(deepcopy(Individu(pat, False)))
            self.noteIndi()

    def selection(self):
        for i in range(floor(self._popSize * self._fracSupr)):
            indi = self._selectRandomIndividu()
            self._sommesNotes -= indi.note
            self._pop.remove(indi)

    @property
    def solutions(self):
        return self._sol
