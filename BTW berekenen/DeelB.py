def calculate_vat(vat_percentage, amount):
    return amount*vat_percentage/100

input_number = input("Geeft het bedrag van het in:")
amount = 0
try:
    amount = int(input_number)
except ValueError:
    print("Geen nummer ingevuld.")
else:
    vat = None
    input_category = input("Geef de categorie in (type a voor 6%, b voor 12% en c voor 21%):")
    if input_category.lower() == "a":
        vat = calculate_vat(6,amount)
    elif input_category.lower() == "b":
        vat = calculate_vat(12,amount)
    elif input_category.lower() == "c":
        vat = calculate_vat(21,amount)
    else:
        print("Geen correcte category ingevuld.")
    if vat is not None:
        print("De BTW bedraagt " + str(vat) + " euro")

