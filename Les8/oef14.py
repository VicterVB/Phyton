def positief_verschil():
    n = int(input("Voer het aantal getallen in: "))
    if n <= 0:
        print("Geef minstens één getal op.")
        return

    getallen = []
    for i in range(n):
        getal = float(input(f"Voer getal {i + 1} in: "))
        getallen.append(getal)

    if len(getallen) == 1:
        print("Er is slechts één getal ingevoerd, het verschil is 0.")
    else:
        kleinste = min(getallen)
        grootste = max(getallen)
        verschil = grootste - kleinste
        if verschil > 0:
            print(f"Het positieve verschil tussen het grootste en kleinste getal is: {verschil}")
        else:
            print("Er is geen positief verschil tussen de getallen.")

positief_verschil()
