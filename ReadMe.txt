Countdigits:
börjar med att ta in en int som input och sedan gör om till sträng, temp
sedan skapar variabler för nollor, jämna tal och ojämna tal. vi tar sedan och itererar genom alla
element i strängen och kollar om int(temp[i]) är noll, modulus två inte är noll annars är den ojämn
och lägger till 1 på korresponderande variabel.
sedan printar vi variablerna som svar.

____________________________________________
Birthday candles:
vi börjar med att definera variabler age, rem(remaining candles) och boxes med värdet 0.
vi tar sedan en while loop och kör koden i medans age <= 100
medans age <= 100:
	i = 0 kommer vara antal lådor som köps på en gång

	om rem < age:
		i += 1; vi vill köpa en (till) låda
		rem += 24; vi lägger till 24 candles i vårat "förråd av candles"

		boxes += i; lägger till i antal boxes i totala mängden boxes som köppts

		om i > 0 alltså om vi köppt boxes
	            print("Before birthday", str(age) + ",", "buy", i, "box(es)")

		rem -= age; tar bort åldern från remaining candles

		age += 1; öka ålder

sedan loopas den igen

när den e klar:
printar den ut hur många boces vi köpt och hur många candles som e kvar

_____________________________________
abcd:
definerar funktion get_number som tar in parametrar a, b, c, d
def get_number(a, b, c, d):
	sedan kollar vi för alla olika kombinationer av a, b, c och d
	for a in range(1, 10) då a inte kan vara 0
		for b in range(0, 10)
			for c in range(0, 10)
				for d in range(1, 10) då d inte får vara 0

					sedan kollar vi i kombinationen av den iterationen
					it 1: 1001
					it 2: 1002
					osv
					tills kravet 
					if 4* abcd som tal == dcba som tal
						printar ut rätt tal.

och kallar funktionen här nere som tar 4 ints som parameter då jag inte vet vad som är 
bättre att skriva här.
get_number(int, int, int, int)

_________________________________________
pi_approx:
vi börjar med att importera random. Och även pi från math.

och skapar funktionen get_pi_approx():
	count = 0
	for i in range(n): för att kolla n antal punkter
		x = random.uniform(-1, 1) ett värde mellan -1 och 1
		

vi får promten att välja antal n

