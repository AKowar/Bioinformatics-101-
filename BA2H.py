# -*- coding: utf-8 -*-
"""
Created on Sun Jun 10 11:36:00 2018

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

DNA=('TTACCTTAAC', 'GATATCTGTC', 'ACGGCGTTCG', 'CCCTAAAGAG', 'CGTCAGAGGT')
pattern=('AAA')
print(DistanceBetweenPatternAndStrings(pattern,DNA)) #Ausgeben der Funktion DistanceBetween..