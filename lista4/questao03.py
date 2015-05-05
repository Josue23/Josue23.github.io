import random
vetor1 = []
vetor2 = []
vetor20 = []
n = 0
while n < 10: #len(vetor1) < 10 and len(vetor2) < 10:
	vetor1.append(random.randrange(1, 101))
	vetor20.append(vetor1[n])
	vetor2.append(random.randrange(1, 101))
	vetor20.append(vetor2[n])
	n += 1
print(vetor1)
print(vetor2)
print(vetor20)
