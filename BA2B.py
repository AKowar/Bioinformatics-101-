# -*- coding: utf-8 -*-
"""
Created on Sun Jun 10 12:54:02 2018

@author: Alex
"""

def HammingDistance(p, q): #Definiere HammingDistance
	Hamm = 0
	for x, y in zip(p, q): #Erstellen von Tupeln aus pattern und i[x:x+k]
		if x != y:
			Hamm += 1
	return Hamm
  
def DistanceBetweenPatternAndStrings(pattern, DNA): #Definiere DistanceBetween...
    k=len(pattern)#k entspricht der Länge des patterns
    distance=0
    for i in DNA:#Einrichten for-Schleife für text in DNA
        Hamming=k+1
        for x in range(len(i)-k+1): #for-Schleife für k-mere
            z=HammingDistance(pattern, i[x:x+k])#Zuordnung und Abkürzung von HammingDistance
            if Hamming > z: #if-Funktion für minimale Angabe der HammingDistance; Wenn z kleiner als Hamming..
                Hamming=z #...dann ist z Hamming
    
        distance+=Hamming #Summierung von distance
    return distance #Wiedergabe von distance

def numberToPattern(i, k): #Analoges Problem in BA1K
	if k == 1:
		return numberToSymbol(i)
	return numberToPattern(i // 4, k-1) + numberToSymbol(i % 4)

def numberToSymbol(i): #Analoges Problem in BA1K
	if i == 0:
		return "A"
	if i == 1:
		return "C"
	if i == 2:
		return "G"
	if i == 3:
		return "T"

def medianString(DNA, k): #Definiere medianString
	distance = (k+1) * len(DNA) #Bestimmung der Distanz
	median = [] #Bestimmung der Variablen
	for i in range(4**k):#for-Schleife für alle k-mere
		pattern = numberToPattern(i, k)
		z = DistanceBetweenPatternAndStrings(pattern, DNA) #Zuordnung und Abkürzung von HammingDistance
		if distance > z: #if-Funktion für minimale Angabe der distance
			distance = z
			median = pattern
	return median #Wiedergabe von median

DNA = ('TGATGATAACGTGACGGGACTCAGCGGCGATGAAGGATGAGT', 'CAGCGACAGACAATTTCAATAATATCCGCGGTAAGCGGCGTA', 
'TGCAGAGGTTGGTAACGCCGGCGACTCGGAGAGCTTTTCGCT', 'TTTGTCATGAACTCAGATACCATAGAGCACCGGCGAGACTCA', 
'ACTGGGACTTCACATTAGGTTGAACCGCGAGCCAGGTGGGTG', 'TTGCGGACGGGATACTCAATAACTAAGGTAGTTCAGCTGCGA', 
'TGGGAGGACACACATTTTCTTACCTCTTCCCAGCGAGATGGC', 'GAAAAAACCTATAAAGTCCACTCTTTGCGGCGGCGAGCCATA', 
'CCACGTCCGTTACTCCGTCGCCGTCAGCGATAATGGGATGAG', 'CCAAAGCTGCGAAATAACCATACTCTGCTCAGGAGCCCGATG')
k = 6
print(medianString(DNA, k))













