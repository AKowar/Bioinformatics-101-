# -*- coding: utf-8 -*-
"""
Created on Sun Jun 24 10:55:09 2018

@author: Alex
"""

import random 

def patternToNumber(pattern): #Bestimmung der Funktion patternToNumber -> patternToNumber Aufgabe 2
	if len(pattern) == 0:
		return 0
	return 4 * patternToNumber(pattern[0:-1]) + symbolToNumber(pattern[-1:])
     #Gleichung für den Prefix und Anhang

def symbolToNumber(symbol): #Umschreiben der Basen in Zahlenwerte
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

def profileProbable(text, k, profile): #Erstellen des wahrscheinlichsten Profils
	maxprob = 0
	kmer = text[0:k]
	for i in range(0,len(text) - k +1):
		prob = 1
		pattern = text[i:i+k]
		for j in range(k):
			l = symbolToNumber(pattern[j])
			prob *= profile[l][j]
		if prob > maxprob:
			maxprob = prob
			kmer = pattern
	return kmer

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


def profileForm(motifs): #Definieren des Profils
	k = len(motifs[0])
	profile = [[1 for i in range(k)] for j in range(4)]
	for x in motifs: #for-Schleife für alle möglichen Motive
		for i in range(len(x)):
			j = symbolToNumber(x[i])
			profile[j][i] += 1
	for x in profile:#for-Schleife für Profil
		for i in range(len(x)):
			x[i] = x[i]/len(motifs)
	return profile #Wiedergabe des Profils

def consensus(profile): #Definieren der Funktion für die consensus-motif aus dem Profil
	str = ""
	for i in range(len(profile[0])):
		max = 0
		loc = 0
		for j in range(4):
			if profile[j][i] > max:
				loc = j
				max = profile[j][i]
		str+=numberToSymbol(loc)
	return str #Wiedergabe des consensus-motif

def score(motifs): #Erstellen eines scores für mögliche consensus-motifs
	profile = profileForm(motifs)
	cons = consensus(profile)
	score = 0
	for x in motifs:
		for i in range(len(x)):
			if cons[i] != x[i]:
				score += 1
	return score #Wiedergabe des scores

def randomMotifSearch(dna, k, t): #Definieren des randomisierten Algorithmus
	bestMotifs = []
	motifs = []
	for x in range(t):
		random.seed()
		i = random.randint(0, len(dna[x])-k)
		motifs.append(dna[x][i:i+k])
	bestMotifs = motifs.copy()
	count = 0
	while True: #Wenn ein motif in einem Profil..
		profile = profileForm(motifs)
		for x in range(t):
			motifs[x] = profileProbable(dna[x], k, profile)#..die höchste Wahrscheinlichtkeit hat..
		if score(motifs) < score(bestMotifs):#..und einen niedrigeren score..
			bestMotifs = motifs.copy() #..wird das motif zum besten motif
			count+=1
		else:
			print(count) #Wenn nicht, gib das beste motif wieder
			return bestMotifs

k = 8
t = 5
dna = ['CGCCCCTCTCGGGGGTGTTCAGTAAACGGCCA','GGGCGAGGTATGTGTAAGTGCCAAGGTGCCAG','TAGTACCGAGACCGAAAGAAGTATACAGGCGT','TAGATCAAGTTTCAGGTGCACGTCGGTGAACC','AATCCACCAGCTCCACGTGCAATGTTGGCCTA']
best = randomMotifSearch(dna, k, t)
min = score(best)
for x in range(1000):
	print(x)
	a = randomMotifSearch(dna, k, t)
	if score(a) < score(best):
		best= a
		min = score(a)
print(min)
for x in best:
	print(x)








