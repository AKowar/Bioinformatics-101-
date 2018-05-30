# -*- coding: utf-8 -*-
"""
Created on Wed May 30 18:47:57 2018

@author: Alex
"""

def patternToNumber(pattern): #Bestimmung der Funktion patternToNumber
	if len(pattern) == 0:
		return 0
	return 4 * patternToNumber(pattern[0:-1]) + symbolToNumber(pattern[-1:])
     #Gleichung für den Prefix und Anhang

def symbolToNumber(symbol): #Umnschreiben der Basen in Zahlenwerte
	if symbol == "A":
		return 0
	if symbol == "C":
		return 1
	if symbol == "G":
		return 2
	if symbol == "T":
		return 3
  
print(patternToNumber("CTTCTCACGTACAACAAAATC"))