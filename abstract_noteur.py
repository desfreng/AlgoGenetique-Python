#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 23 22:28:23 2018

@author: gabriel
"""


class AbstractNoteur:
    def __init__(self):
        self.resetSommeNotes()

    def __call__(self, indi):
        raise Exception("Doit être redéfini dans une classe fille !")

    def resetSommeNotes(self):
        self._sommeNotes = 0

    @property
    def sommesNotes(self):
        return self._sommeNotes
