letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

coord = input("Enter a chess square identifier (e.g. e5): ")

letpos = letters.index(coord[0])

if letpos % 2 == int(coord[1]) % 2:
    print(coord + " is White")
else:
    print(coord + " is Black")

"""

vi kan kolla om det numeriska 'värdet' av en bokstav är
jämt eller ojämt och jämnföra det med den numeriska koordinaten.

om båda är jämna eller ojämna så är koordinaten vit, annars så är den
svart.

"""