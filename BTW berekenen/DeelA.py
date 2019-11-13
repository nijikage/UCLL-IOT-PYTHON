input_number = input("Geeft het bedrag van het in: ")
amount = 0
try:
    amount = int(input_number)
except ValueError:
    print("Geen nummer ingevuld.")
else:
    vat = amount*6/100
    print("De BTW bedraagt " + str(vat) + " euro")