# -*- coding: utf-8 -*-
"""
Created on Wed May 30 19:16:49 2018

@author: Alex
"""
def patternToNumber(pattern): #Bestimmung der Funktion patternToNumber -> patternToNumber Aufgabe 2
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
  
def numberToPattern(x, k): #Bestimmung der Funktion numberToPattern -> numberToPattern Aufgabe 3
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

frequencyArray = [] #Definition des frequencyArray

def computeFrequencies(text,k): #Bestimmung der Funktion computeFrequencies
  for i in range(4**k): #for-Schleife von 0 bis 4^k
    frequencyArray.append(0) #Einfügen von 0 an Stelle i im frequencyArray 
  for i in range(len(text)-1): #for-Schleife von 0 bis Textlänge
    pattern = text[i:i+k] #Definieren von pattern
    j = patternToNumber(pattern) #Berechnung patternToNumber von pattern
    frequencyArray[j] = frequencyArray[j] + 1 #Erhöhung des Wertes an Stelle i im frequencyArray 
  return frequencyArray #Wiedergabe frequencyArray

print(computeFrequencies("ACGCGGCTCTGAAA",2))
