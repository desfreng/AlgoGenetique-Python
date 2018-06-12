#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 23 22:54:31 2018

@author: gabriel
"""
import math

from abstract_noteur import AbstractNoteur
from individu import Individu


class Noteur(AbstractNoteur):
    def __init__(self, resultat):
        self._res = resultat
        super().__init__()

    def __call__(self, indi):

        if not isinstance(indi, Individu):
            raise ValueError(Individu)

        # Si l'individu est déjà noté
        if bool(indi):
            # On retourne sa note déjà existante
            self._sommeNotes += indi.note
            return indi.note

        laNote = 1.0  # Initialisation à 1 pour éviter que la note soit nulle

        #       PREMIÈRE PARTIE
        # Vérification du résultat du Serpent
        # Plus le résultat est près du résultat attendu, plus la note est basse

        par1 = 13.0 * indi[1] / indi[2]  # Calcul de la 'Première Parenthèse'
        par3 = indi[6] * indi[7] / indi[8]  # Calcul de la 'Troisième Parenthèse'
        resul = (
            indi[0] + par1 + indi[3] + 12.0 * indi[4] - indi[5] - 11.0 + par3 - 10.0
        )  # Calcul du 'Sepent'

        laNote += abs(resul - self._res)

        # DEUXIÈME PARTIE
        # On vérifie que le patrimoine de l'individu contient bien
        # que des nombres différents. Sinon, on ajoute à la note le nombre
        # de nombres idebtiques

        for allele in indi.patrimoine:
            # Je compte le nombre de chaque allèle dans le patrimoine
            # puis j'ajoute ce nombre soustrait de 1 afin de ne garder
            # seulement les alleles en trop
            laNote += indi.patrimoine.count(allele) - 1

        # On retourne la note
        self._sommeNotes += math.ceil(laNote)
        return math.ceil(laNote)

    def __str__(self):
        return "Noteur, Resultat : {}".format(self._res)

    def __eq__(self, other):
        return self._res == other._res

    def __repr__(self):
        return str(self)
