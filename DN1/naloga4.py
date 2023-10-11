'''
Napišite funkcijo izpisi_trikotnik, ki sprejme celo število visina, ki predstavlja višino trikotnika. Funkcija naj vrne izpis trikotnika zvezdic v naslednji obliki:

Primer:

Če je visina enaka 5, naj funkcija izpiše:

*
**
***
****
*****
'''
def izpisi_trikotnik(visina):
    i = 0
    for x in range(visina+1):
        print("*"*i)
        i = i + 1   

izpisi_trikotnik(6)
