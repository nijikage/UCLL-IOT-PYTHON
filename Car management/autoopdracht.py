class classname(object):
    pass

file_name = "auto.csv"
token  = ","
vehicles = []
message = """Welkom, gelieve keuze te maken"
1. Voertuig toevoegen.
2. Voertuigen afprinten.
3. Opslaan
4. Afsluiten
>"""
fuels = ["Diesel", "Benzine"]

with open(file_name) as csv_file:
    for line in csv_file:
        vehicle = line.strip().split(token)
        vehicles.append(vehicle)

while True:
    choice = input(message)

    if choice == "1":
        print("Geeft details van auto:2")
    
        while True:
            brand = input("Geef merk: ")
            if brand:
                break
            print("Geen merk ingevuld.")
        
        while True:
            colour = input("Geef kleur: ")
            if colour:
                break
            print("Geen kleur ingevuld.")
        
        while True:
            fuel = input("Geef brandstof 1 voor Diesel, 2 voor Benzine: ")
            if fuel.isnumeric():
                if int(fuel) <= len(fuels) and int(fuel) > 0:
                    fuel = fuels[(int(fuel)-1)]
                    break
                else:
                    print("Geef een correcte optie.")
            else:
                print("Geef een getal.")
        
        while True:
            kw = input("Geef KW: ")
            if kw.isdigit():
                break
            print("U heeft geen nummer ingegeven,")
            
        vehicles.append([brand, colour, fuel, kw])
    elif choice == "2":
        for vehicle in vehicles:
            print("{0}, kleur = {1}, brandstof = {2}, KW = {3}".format(vehicle[0],vehicle[1],vehicle[2],vehicle[3]))
   
    elif choice == "3":
        with open(file_name, "w") as file:
            for vehicle in vehicles:
                file.write("{},{},{},{}\n".format(vehicle[0],vehicle[1],vehicle[2],vehicle[3]))
    elif choice == "4":
        break
    else:
        print("Invoer niet herkent. Probeer opnieuw")

print("Programma is gesloten.")