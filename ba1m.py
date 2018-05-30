# -*- coding: utf-8 -*-
"""
Created on Wed May 30 19:01:03 2018

@author: Alex
"""

def numberToPattern(x, k): #Bestimmung der Funktion numberToPattern
	if k == 1:
		return numberToSymbol(x)
	return numberToPattern(x // 4, k-1) + numberToSymbol(x % 4)

def numberToSymbol(x): #Umschreiben der Zahlenwerte in Buchstaben
	if x == 0:
		return "A"
	if x == 1:
		return "C"
	if x == 2:
		return "G"
	if x == 3:
		return "T"

print(numberToPattern(5353,7)) #Einsetzen der Nummer 5353 und k(7) 