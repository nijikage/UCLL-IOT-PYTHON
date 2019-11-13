def calculate_vat(vat_percentage, amount):
    return amount*vat_percentage/100

total_vat = 0

while True:
    input_number = input("Geeft het bedrag van het in (typ 0 om berekening te stoppen): ")
    amount = 0
    try:
        amount = int(input_number)
        if amount == 0:
            break
    except ValueError:
        print("Geen bedrag ingevuld.")
    else:
        input_category = input("Geef de categorie in (type a voor 6%, b voor 12% en c voor 21%): ")
        if input_category.lower() == "a":
            total_vat += calculate_vat(6,amount)
        elif input_category.lower() == "b":
            total_vat += calculate_vat(12,amount)
        elif input_category.lower() == "c":
            total_vat += calculate_vat(21,amount)
        else:
            print("Geen correcte category ingevuld.")

print("De BTW bedraagt " + str(total_vat) + " euro")