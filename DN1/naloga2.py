'''
Napišite program seštevalnik, ki sešteje dva list-a tako, da s for loop zanko iterirate po list-u. 
Seštevajte elemente po indexih in rezultate dodajte v novi list (uporabi .append).

List 1: [0,1,2,3,4,5,6,7,8,9]
List 2: [9,8,7,6,5,4,3,2,1,0]

Rezultat mora biti naslednji list: [9,9,9,9,9,9,9,9,9,9] 
'''
List1 = [0,1,2,3,4,5,6,7,8,9]
List2 = [9,8,7,6,5,4,3,2,1,0]
List3 = []

for i in List1:
    List3.append(List1[i]+List2[i])

print(List3)