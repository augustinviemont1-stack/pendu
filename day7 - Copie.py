from english_words import get_english_words_set

words = get_english_words_set(["web2"], lower = True)

import random

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']



x= list(random.choice(list(words)))

print(*x)

answer=["_"]*len(x)

penalty = 0

def letterp(n):
	global penalty
	
	while answer != x:
		uinput=input("Pls choose a letter : ")
		if uinput in alphabet and len(uinput) == 1:
			if uinput in x:
				for i, y in enumerate(x):
					if y == uinput:
						answer[i]=uinput
				print (*answer)

			else :
				penalty += 1
				print ("Nop, but nt, u have", 12-penalty, "tries left,")

		else:
			print("A FUCKING LETTER >: ( ")

		if penalty >= 12:
			print ("U loose !!!!")
			break

		if answer == x:
			print ("Wp 2 u, u find the good word !! Wich was : ", *x)
			break

letterp(x)
