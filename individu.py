#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 27 19:31:43 2018

@author: gabriel
"""
from random import shuffle


class Individu:
    def __init__(self, patrimoine, random=True):

        self._pat = patrimoine
        self._index = 0

        if random:
            shuffle(self._pat)

        self._note = 0

    @property
    def patrimoine(self):
        return self._pat

    @property
    def getAllele(self, index):
        return self._pat[index]

    def swapAlleles(self, index1, index2):
        try:
            self._pat[index1], self._pat[index2] = self._pat[index2], self._pat[index1]
        except:
            print("Ah !")
            print("Index1 : {}, Index2 : {}".format(index1, index2))
            print("Patrimoine : {}, Taille : {}".format(self._pat, len(self._pat)))
            raise

        self.resetNote()

    def haveNote(self):
        return self._note != 0

    @property
    def note(self):
        return self._note

    @note.setter
    def note(self, value):
        self._note = value

    def resetNote(self):
        self._note = 0

    def __getitem__(self, index):
        return self._pat[index]

    def __str__(self):
        if self._note == 0:
            return "{} -> Non noté".format(self._pat)
        return "{} -> {}".format(self._pat, self._note)

    def __eq__(self, other):
        return self._pat == other._pat

    def __lt__(self, other):
        return self.note < other.note

    def __repr__(self):
        return str(self)

    def __bool__(self):
        return self.haveNote()

    def __iter__(self):
        return self

    def __next__(self):
        if self._index == 10:
            self._index = 0
            raise StopIteration
        self._index += 1
        return self._pat[self._index - 1]
