price = float(input("Price: "))
payment = float(input("Payment: "))

price = round(price)
payment = round(payment)

change = payment - price

print("Change: " + str(change))

if change/1000 >= 1:
    tusen = str(change//1000)
    change = change % 1000
else:
    tusen = '0'

if change/500 >= 1:
    femhundra = str(change//500)
    change = change % 500
else:
    femhundra = '0'

if change/200 >= 1:
    tvåhundra = str(change//200)
    change = change % 200
else:
    tvåhundra = '0'

if change/100 >= 1:
    hundra = str(change//100)
    change = change % 100
else:
    hundra = '0'

if change/50 >= 1:
    femtio = str(change//50)
    change = change % 50
else:
    femtio = '0'

if change/20 >= 1:
    tjugo = str(change//20)
    change = change % 20
else:
    tjugo = '0'

if change/10 >= 1:
    tio = str(change//10)
    change = change % 10
else:
    tio = '0'

if change/5 >= 1:
    fem = str(change//5)
    change = change % 5
else:
    fem = '0'

if change/2 >= 1:
    två = str(change//2)
    change = change % 2
else:
    två = '0'

ett = str(change)

print("1000kr bills: " + tusen)
print("500kr bills: " + femhundra)
print("200kr bills: " + tvåhundra)
print("100kr bills: " + hundra)
print("50kr bills: " + femtio)
print("20kr bills: " + tjugo)
print("10kr bills: " + tio)
print("5kr bills: " + fem)
print("2kr bills: " + två)
print("1kr bills: " + ett)
