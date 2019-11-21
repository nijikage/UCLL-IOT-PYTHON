while True:
    fuels = ["Diesel", "Benzine"]
    print(" Welkom, gelieve keuze te maken")
    print("1. Voertuig toevoegen.")
    print("2. Voertuigen afprinten.")
    print("3. Afsluiten")
    number = input()

    if number == "1":
        print("Geeft details van auto:")
    
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
            fuel = input("Geef brandstof 1 voor")
            if fuel.isnumeric():
                if int(fuel) <= len(fuels) and int(fuel) > 0:
                    fuel = fuels[(int(fuel)-1)]
                    break
                else:
                    print("Geef een correcte optie")
            else:
                print("Geef een getal.")
        
        while True:
            kw = input("Wat is de KW?")
            if kw.isdigit():
                break
            print("U heeft geen nummer ingegeven,")
            
        with open("auto.csv", "a") as file:
            file.write("{},{},{},{}\n".format(brand, colour, fuel, kw))
    elif number == "2":      
        with open("auto.csv", "r") as file:
            for line in file:
                for word in line.split(","):
                        print(word)
    elif number == "3":
        break
    else:
        print("Invoer niet herkent. Probeer opnieuw")