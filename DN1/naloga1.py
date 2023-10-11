'''
Uporabnika zaprosite, naj vnese neko celo število. To vrednost shranite v spremenljivko z imenom n in jo izpišite ter izpišite njen tip. 
Nato to vrednost pretvorite v float vrednost. Dobljeno float vrednost shranite v spremenljivko n. Nato n izpišite in izpišite njen tip.
'''
n = int(input("Prosim vnesi celo število: "))
print(n, type(n))
n = float(n)
print(n, type(n))